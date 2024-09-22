import axios from "axios"
import { getUsersUrl } from "../constants/urls"
import { createAsyncThunk } from "@reduxjs/toolkit"

const fetchUsers = createAsyncThunk("Users/fetchUsers", async () =>  {

    try {
      const response = await axios.get(getUsersUrl, {
        headers: {
          "X-Requested-With": "XMLHttpRequest", 
        },
      })
    
      return response.data
    } catch(error) {
      throw new Error(`Error: ${error.message}`)
    }
})

export default fetchUsers