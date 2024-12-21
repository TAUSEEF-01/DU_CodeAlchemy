import {asyncHandler} from '../utils/AsyncHandler.js'
import {ApiResponse} from '../utils/ApiResponse.js'
import {ApiError} from '../utils/ApiError.js'
import {Ingredient} from '../db/model.js' 

export const addIngredient = asyncHandler( async (req, res) => {
    const {name, quantity, unit } = req.body

    if (
        [name, quantity, unit].some((field) => field?.trim() === "")
    ) {
        throw new ApiError(400, "All fields are required")
    }

    const existedIngredient = await Ingredient.findOne(name)

    if (existedIngredient) {
        existedIngredient.isAvaliable = true;
        existedIngredient.quantity = quantity;
        await existedIngredient.save();
    }
    else{
        existedIngredient = await User.create({name, quantity, unit })

        if (!existedIngredient) {
            throw new ApiError(500, "Something went wrong while adding the Ingredient")
        }
    }
    return res.status(201).json(
        new ApiResponse(200, existedIngredient, "Ingredient added Successfully")
    )

} )

export const updateIngredient = asyncHandler( async (req, res) => {
    const {name, quantity} = req.body

    if (
        [name, quantity].some((field) => field?.trim() === "")
    ) {
        throw new ApiError(400, "All fields are required")
    }

    const existedIngredient = await Ingredient.findOne(name)

    if (!existedIngredient) {
        throw new ApiError(404, "Ingredient not found")
    }
    else{
        const quant = parseInt(quantity)
        if(quant == 0){
            existedIngredient.isAvaliable = false;
            existedIngredient.quantity = 0;
        }
        else{
            existedIngredient.quantity = quantity;
        }
        await existedIngredient.save()
    }

    return res.status(201).json(
        new ApiResponse(200, existedIngredient, "Ingredient registered Successfully")
    )

} )

export const getIngredients = asyncHandler( async (req, res) => {
    const avaliableIngredients = await Ingredient.find({isAvaliable : true}).distinct('name')
    if (avaliableIngredients.length == 0) {
        throw new ApiError(404, "No ingredient avaliable")
    }

    return res.status(201).json(
        new ApiResponse(200, avaliableIngredients, "Ingredient retrieved Successfully")
    )

} )



