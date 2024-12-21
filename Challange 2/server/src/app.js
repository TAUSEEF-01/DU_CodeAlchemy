import express, {Router} from "express"
import ingredientRouter from './routes/ingredient.route.js'
import cors from "cors"

const app = express()


app.use(cors({
    origin: "*",
    credentials: true
}))
app.use(express.json())
app.use(express.urlencoded({extended: true}))
app.use("/api/ingredients", ingredientRouter)

export default app
