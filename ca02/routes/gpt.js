// Import required libraries
const express = require("express");
const path = require("path");
const { GPT } = require("openai");
require("dotenv").config();

// Initialize the app and OpenAI's GPT API
const app = express();
const gptAPI = new GPT(process.env.APIKEY);

// Set the views directory and view engine
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

// Define a route for the home page
app.get("/", (req, res) => {
  console.log("processing / route");
  res.render("home");
});

// Define a route for the team pages
app.get("/index", (req, res) => {
  console.log("processing /index route");
  res.render("team");
});

// Define a route for the about page
app.get("/about", (req, res) => {
  console.log("processing /about route");
  res.render("about");
});

// Define a route for the GPT demo page
app.get("/gptdemo", (req, res) => {
  console.log("processing /gptdemo route");
  res.render("gptdemo");
});

// Define a route to handle form submissions
app.post("/gptdemo", async (req, res) => {
  console.log("processing form submission");

  // Get the prompt from the form data
  const prompt = req.body.prompt;

  // Send the prompt to OpenAI's GPT API to get a response
  const response = await gptAPI.complete({
    prompt,
    maxTokens: 150,
    n: 1,
    stop: "\n",
  });

  // Render the response on the page
  res.render("gptdemo", { response: response.choices[0].text });
});

// Start the server
app.listen(3000, () => {
  console.log("Server listening on port 3000");
});
