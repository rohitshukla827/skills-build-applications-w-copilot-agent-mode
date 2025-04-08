const { MongoClient } = require('mongodb');

async function initializeDatabase() {
	const uri = "mongodb://localhost:27017"; // Replace with your MongoDB connection string
	const client = new MongoClient(uri);

	try {
		await client.connect();
		const db = client.db('octofit_db');

		await db.createCollection('users');
		await db.createCollection('teams');
		await db.createCollection('activity');
		await db.createCollection('leaderboard');
		await db.createCollection('workouts');
		await db.collection('users').createIndex({ email: 1 }, { unique: true });

		console.log("Database initialized successfully");
	} catch (error) {
		console.error("Error initializing database:", error);
	} finally {
		await client.close();
	}
}

initializeDatabase();
