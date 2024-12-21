import {Location} from '../db/model.js'
import { readFileSync } from "fs";
import { fileURLToPath } from "url";
import path from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const insertLocations = async (req, res) => {
    try {
        // const filePath = path.resolve(__dirname, "../flat_location.json");
        // const rawData = readFileSync(filePath, "utf-8");
        // const locations = JSON.parse(rawData);

        // await Location.insertMany(locations);
        await Location.updateMany({"district" : "Coxâ€™s Bazar"}, {"district" : "Cox's Bazar"})
        console.log("Successfully inserted locations");

        res.status(200).send("Locations inserted successfully");
    } catch (error) {
        console.error("Error in inserting location", error);
        res.status(500).send("Failed to insert locations");
    }
};


export const getDivisions = async (req, res) => {
    try {
        const divisions = await Location.distinct('division')
        // console.log(typeof(divisions));

        res.status(200).json({
            message: "Divisions retrieved successfully",
            data: divisions
        })
    } catch (error) {
        console.error("Error in finding divisions", error);
        res.status(500).send("Failed to find divisions");
    }
}


export const getDistricts = async (req, res) => {
    try {
        const {div} = req.params
        const districts = await Location.find({division: div}).distinct("district")

        res.status(200).json({
            message: "Districts retrieved successfully",
            data: districts
        })
    } catch (error) {
        console.error("Error in finding districts", error);
        res.status(500).send("Failed to find districts");
    }
}

export const getAreas = async (req, res) => {
    try {
        const {dist} = req.params
        const areas = await Location.find({district: dist}).distinct("area")
        // const filteredArea = 
        res.status(200).json({
            message: "areas retrieved successfully",
            data: areas
        })
    } catch (error) {
        console.error("Error in finding areas", error);
        res.status(500).send("Failed to find areas");
    }
}
export const getSubAreas = async (req, res) => {
    try {
        const {area} = req.params
        const areas = await Location.findOne({area: area})
        
        const hasSubarea = "subareas" in areas
        res.status(200).json({
            message: "areas retrieved successfully",
            hasSubarea : hasSubarea,
            data: hasSubarea ? areas.subareas : []
        })
    } catch (error) {
        console.error("Error in finding areas", error);
        res.status(500).send("Failed to find areas");
    }
}