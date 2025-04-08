use octofit_db;
db.users.insertOne({ email: "sampleuser@example.com", name: "Sample User" });
db.teams.insertOne({ name: "Sample Team", members: [] });
db.activity.insertOne({ user: "sampleuser@example.com", type: "running", duration: 30 });
db.leaderboard.insertOne({ user: "sampleuser@example.com", points: 100 });
db.workouts.insertOne({ name: "Sample Workout", description: "A sample workout description." });
