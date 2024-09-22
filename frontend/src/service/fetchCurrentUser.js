import axios from "axios"
import { getCurrentUserUrl } from "../constants/urls"
import { createAsyncThunk } from "@reduxjs/toolkit"

const fetchCurrentUser = createAsyncThunk("Profile/fetchCurrentUser", async (userId) =>  {
    try {
      const response = await  axios.get(`${getCurrentUserUrl}${userId}`, {
        headers: {
          "X-Requested-With": "XMLHttpRequest", 
        },
      })
    return response.data
    } catch(error) {
      throw new Error(`Error: ${error.message}`)
    }
})

export default fetchCurrentUser