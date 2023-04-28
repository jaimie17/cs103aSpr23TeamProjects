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
  // Define a route for the poem page
  app.get("/poem", (req, res) => {
    console.log("processing /poem route");
    res.render("poem");
  });

  // Define a route to handle poem form submissions
  app.post("/poem", async (req, res) => {
    console.log("processing poem form submission");

    // Get the prompt from the form data
    const prompt = req.body.prompt;

    // Generate a poem based on the prompt using the GPT API
    const poem = await gptAPI.generatePoem(prompt);

    // Render the poem on the page
    res.render("poem", { poem });
  });

  // Define a route for the summaries page
  app.get("/summaries", (req, res) => {
    console.log("processing /summaries route");
    res.render("summaries");
  });

  // Define a route to handle summaries form submissions
  app.post("/summaries", async (req, res) => {
    console.log("processing summaries form submission");

    // Get the text to summarize from the form data
    const text = req.body.text;

    // Generate a summary of the text using the GPT API
    const summary = await gptAPI.generateSummary(text);

    // Render the summary on the page
    res.render("summaries", { summary });
  });

  // Define a route for the Spanish translator page
  app.get("/spanishTranslator", (req, res) => {
    console.log("processing /spanishTranslator route");
    res.render("spanishTranslator");
  });

  // Define a route to handle Spanish translator form submissions
  app.post("/spanishTranslator", async (req, res) => {
    console.log("processing Spanish translator form submission");

    // Get the text to translate from the form data
    const text = req.body.text;

    // Translate the text to Spanish using the GPT API
    const translation = await gptAPI.translateToSpanish(text);

    // Render the translated text on the page
    res.render("spanishTranslator", { translation });
  });

  // Render the response on the page
  res.render("gptdemo", { response: response.choices[0].text });
});

