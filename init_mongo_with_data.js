const { MongoClient } = require('mongodb');

async function initializeDatabase() {
	const uri = "mongodb://localhost:27017";
	const client = new MongoClient(uri);

	try {
		await client.connect();
		const db = client.db("octofit_db");

		await db.collection("users").insertOne({ email: "sampleuser@example.com", name: "Sample User" });
		await db.collection("teams").insertOne({ name: "Sample Team", members: [] });
		await db.collection("activity").insertOne({ user: "sampleuser@example.com", type: "running", duration: 30 });
		await db.collection("leaderboard").insertOne({ user: "sampleuser@example.com", points: 100 });
		await db.collection("workouts").insertOne({ name: "Sample Workout", description: "A sample workout description." });

		console.log("Database initialized successfully.");
	} catch (error) {
		console.error("Error initializing database:", error);
	} finally {
		await client.close();
	}
}

initializeDatabase();
