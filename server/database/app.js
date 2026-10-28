const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 3030;

app.use(cors());
app.use(express.json());
app.use(require('body-parser').urlencoded({ extended: false }));

const reviews_data = JSON.parse(
  fs.existsSync('./data/reviews.json') ? fs.readFileSync('./data/reviews.json', 'utf8') : fs.readFileSync('reviews.json', 'utf8')
);
const dealerships_data = JSON.parse(
  fs.existsSync('./data/dealerships.json') ? fs.readFileSync('./data/dealerships.json', 'utf8') : fs.readFileSync('dealerships.json', 'utf8')
);

const Reviews = require('./review');
const Dealerships = require('./dealership');

async function seedData() {
  try {
    await Reviews.deleteMany({});
    await Reviews.insertMany(reviews_data['reviews']);
    await Dealerships.deleteMany({});
    await Dealerships.insertMany(dealerships_data['dealerships']);
    console.log("Initial Dealerships and Reviews loaded successfully into MongoDB.");
  } catch (error) {
    console.error("Error seeding initial data:", error);
  }
}

async function startDatabase() {
  let mongo_url = process.env.MONGODB_URL;
  if (!mongo_url) {
    try {
      await mongoose.connect("mongodb://mongo_db:27017/", { dbName: 'dealershipsDB', serverSelectionTimeoutMS: 1500 });
      console.log("Connected to MongoDB at mongodb://mongo_db:27017/");
      await seedData();
      return;
    } catch (err) {
      console.log("mongo_db host not reachable, trying localhost...");
    }

    try {
      await mongoose.connect("mongodb://127.0.0.1:27017/", { dbName: 'dealershipsDB', serverSelectionTimeoutMS: 1500 });
      console.log("Connected to local MongoDB at mongodb://127.0.0.1:27017/");
      await seedData();
      return;
    } catch (err) {
      console.log("localhost:27017 not found, starting embedded MongoDB...");
    }

    try {
      const { MongoMemoryServer } = require('mongodb-memory-server');
      const mongod = await MongoMemoryServer.create({
        instance: {
          port: 27017,
          dbName: 'dealershipsDB'
        }
      });
      mongo_url = mongod.getUri();
      console.log("Embedded MongoDB started at:", mongo_url);
    } catch (err) {
      console.log("Embedded MongoDB on 27017 failed, creating dynamic port instance:", err.message);
      const { MongoMemoryServer } = require('mongodb-memory-server');
      const mongod = await MongoMemoryServer.create();
      mongo_url = mongod.getUri();
      console.log("Dynamic MongoDB started at:", mongo_url);
    }
  }

  await mongoose.connect(mongo_url, { dbName: 'dealershipsDB' });
  console.log("Connected to MongoDB database.");
  await seedData();
}

// 1. Home route
app.get('/', async (req, res) => {
  res.send("Welcome to the Mongoose API");
});

// 2. Fetch all reviews
app.get('/fetchReviews', async (req, res) => {
  try {
    const documents = await Reviews.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// 3. Fetch reviews by dealer id
app.get('/fetchReviews/dealer/:id', async (req, res) => {
  try {
    const documents = await Reviews.find({ dealership: req.params.id });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// 4. Fetch all dealerships
app.get('/fetchDealers', async (req, res) => {
  try {
    const documents = await Dealerships.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// 5. Fetch dealers by state
app.get('/fetchDealers/:state', async (req, res) => {
  try {
    const stateParam = req.params.state;
    // Case-insensitive query or exact match
    const documents = await Dealerships.find({
      $or: [
        { state: new RegExp('^' + stateParam + '$', 'i') },
        { st: new RegExp('^' + stateParam + '$', 'i') }
      ]
    });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// 6. Fetch dealer by id
app.get('/fetchDealer/:id', async (req, res) => {
  try {
    const documents = await Dealerships.find({ id: req.params.id });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching documents' });
  }
});

// 7. Insert review
app.post('/insert_review', express.raw({ type: '*/*' }), async (req, res) => {
  try {
    let data = req.body;
    if (typeof data === 'string' || Buffer.isBuffer(data)) {
      data = JSON.parse(data.toString());
    }
    const documents = await Reviews.find().sort({ id: -1 });
    let new_id = (documents && documents.length > 0) ? documents[0]['id'] + 1 : 1;

    const review = new Reviews({
      id: new_id,
      name: data['name'],
      dealership: Number(data['dealership']),
      review: data['review'],
      purchase: Boolean(data['purchase']),
      purchase_date: data['purchase_date'],
      car_make: data['car_make'],
      car_model: data['car_model'],
      car_year: Number(data['car_year']),
    });

    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
    console.error("Error inserting review:", error);
    res.status(500).json({ error: 'Error inserting review' });
  }
});

startDatabase().then(() => {
  app.listen(port, () => {
    console.log(`Express server is running on http://localhost:${port}`);
  });
}).catch(err => {
  console.error("Failed to start database server:", err);
});
