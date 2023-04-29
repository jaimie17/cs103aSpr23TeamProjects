const express = require("express");
const app = express.Router();
const path = require('path');
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

async function getResponse(text){
  console.log("OpenAI API Key:", process.env.OPENAI_API_KEY);
  const gptResponse = await openai.createCompletion({
    model_engine: "text-davinci-003",
    engine: "text-davinci-003",
    prompt: text, 
    maxTokens: 64,
    n: 1,
    temperature: 0.5,
    frequency_penalty: 0,
    presence_penalty: 0,
    model: "text-davinci-003",
  })
  return gptResponse.data.choices[0].text;
}


// Define a route for the summaries page
app.get("/index/summaries", (req, res) => {
  console.log("processing /summaries route");
  res.render("summaries");
});

// Define a route to handle summaries form submissions
app.post("/index/summaries", async (req, res) => {
  console.log("processing summaries form submission");

  // Get the text to summarize from the form data
  const text = req.body.text;

  // Generate a summary of the text using the GPT API
  const summary = await gptAPI.generateSummary(text);

  // Render the summary on the page
  res.render("summaries", { summary });
});

// Define a route for the Spanish translator page
app.get("/index/spanishTranslations", (req, res) => {
  console.log("processing /spanishTranslator route");
  res.render("spanishTranslations");
});

// Define a route to handle Spanish translator form submissions
app.post("/index/spanishTranslations", async (req, res) => {
  console.log("processing Spanish translator form submission");

  // Get the text to translate from the form data
  const text = req.body.text;

  // Translate the text to Spanish using the GPT API
  const translation = await gptAPI.translateToSpanish(text);

  // Render the translated text on the page
  res.render("spanishTranslations", { translation });
});

// Define a route for the poem page
app.get("/index/poems", (req, res) => {
  console.log("processing /poem route");
  res.render("poems");
});

// Define a route to handle poem form submissions
app.post("/index/poems", async (req, res) => {
  console.log("processing poem form submission");

  // Get the prompt from the form data
  const prompt = req.body.prompt;

  // Generate a poem based on the prompt using the GPT API
  const poem = await getResponse(prompt);

  // Render the poem on the page
  res.render("poems", { poem: poem });

});

// Define a route for the Spanish translator page
app.get("/index/synonyms", (req, res) => {
  console.log("processing /synonyms route");
  res.render("synonyms");
});

// Define a route to handle Spanish translator form submissions
app.post("/index/synonyms", async (req, res) => {

  // Get the text to translate from the form data
  const text = req.body.text;

  // Translate the text to Spanish using the GPT API
  const translation = await gptAPI.getSynonyms(text);

  // Render the translated text on the page
  res.render("synonyms", { translation });
});


module.exports = app;
