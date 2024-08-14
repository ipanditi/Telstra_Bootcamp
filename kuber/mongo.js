const { MongoClient } = require('mongodb');

// MongoDB connection
const uri = "mongodb://localhost:27017";
const client = new MongoClient(uri);

async function runMongo() {
    try {
        await client.connect();
        const database = client.db('your_database_name');
        const collection = database.collection('your_collection_name');

        // Insert a document into the collection
        await collection.insertOne({ name: "example", value: 100 });

        // Query the collection
        const cursor = collection.find();
        await cursor.forEach(doc => console.log(doc));
    } finally {
        await client.close();
    }
}

runMongo().catch(console.dir);
