const express = require("express");
const router = express.Router();
const path = require('path');
const APIKEY = process.env.APIKEY;
const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  apiKey: APIKEY,
});
const openai = new OpenAIApi(configuration);

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// Getthe response from the GPT API
async function getResponse(text){
  const gptResponse = await openai.createCompletion({
    prompt: text, 
    max_tokens: 64,
    n: 1,
    temperature: 0.5,
    frequency_penalty: 0,
    presence_penalty: 0,
    model: "text-davinci-003",
  })
  return gptResponse.data.choices[0].text;
}

// Route for the summaries page
router.get("/index/summaries", (req, res) => {
  res.render("summaries");
});

// Route to handle the summaries form submissions
router.post("/index/summaries", async (req, res) => {
  const prompt = "Summarize this text: " + req.body.prompt;
  const summary = await getResponse(prompt);
  res.render("summaries", { summary });
});

// Route for the Spanish translator page
router.get("/index/spanishTranslations", (req, res) => {
  res.render("spanishTranslations");
});

// Route to handle Spanish translator form submissions
router.post("/index/spanishTranslations", async (req, res) => {
  const prompt = "Translate this text to Spanish: " + req.body.prompt;
  const translation = await getResponse(prompt);
  res.render("spanishTranslations", { translation });
});

// Route for the poem page
router.get("/index/poems", (req, res) => {
  res.render("poems");
});

// Route to handle poem form submissions
router.post("/index/poems", async (req, res) => {
  const prompt = "write a poem about: " + req.body.prompt;
  const poem = await getResponse(prompt);
  res.render("poems", { poem });

});

// Route for the Spanish translator page
router.get("/index/synonyms", (req, res) => {
  res.render("synonyms");
});

// Route to handle Spanish translator form submissions
router.post("/index/synonyms", async (req, res) => {
  const prompt = "Generate synonyms for the word " + req.body.prompt;
  const synonyms = await getResponse(prompt);
  res.render("synonyms", { synonyms });
});

module.exports = router;
