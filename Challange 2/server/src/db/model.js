// const mongoose = require('mongoose');
import mongoose from 'mongoose'

const ingredientSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true,
  },
  quantity: {
    type: Number,
    required: true,
  },
  isAvaliable: {
    type: Boolean,
    default: true,
  },
  unit: {
    type: String,
    required: true,
    enum: ['g', 'kg', 'ml', 'l', 'tsp', 'tbsp', 'cup', 'pcs'], // Define valid units
  },
});


export const Ingredient = mongoose.model('Ingredient', ingredientSchema);


const recipeSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true,
  },
  ingredients: [ingredientSchema],
  prepTime: {
    type: Number, // Time in minutes
    required: true,
  },
  taste: {
    type: String,
    enum: ['Sweet', 'Savory', 'Sour', 'Bitter', 'Spicy', 'Umami'], // Predefined taste options
  },
  cuisineType: {
    type: String,
    enum: [      'Kebab',
        'Drinks',
        'Dessert',
        'Rice Item',
        'Beef',
        'Mutton',
        'Vegetables',
        'Seafood',
        'Chicken',
        'Soup',
        'Salad',
        'Snack',
        'Pasta',
        'Bread',
        'Others'
    ]
  },

});
// taste, reviews, Cuisine type, Preparation time
export const Recipe = mongoose.model('Recipe', recipeSchema);
