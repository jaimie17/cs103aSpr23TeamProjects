
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var GPTSchema = Schema( {
  prompt: String,
  answer: String,
  userId: {type:ObjectId, ref:'user' }
} );

module.exports = mongoose.model( 'GPT', GPTSchema );
