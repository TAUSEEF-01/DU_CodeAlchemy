import { Router } from "express";
import {addIngredient, updateIngredient, getIngredients} from "../controllers/ingredient.controller.js"

const router = Router();


router.route("/add-ingredient").post(addIngredient)
router.route("/update-ingredient").get(updateIngredient)
router.route("/get-ingredients").get(getIngredients) 

export default router