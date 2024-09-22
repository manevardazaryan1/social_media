import axios from "axios"
import { getPostsUrl } from "../constants/urls"
import { createAsyncThunk } from "@reduxjs/toolkit"

export const fetchPosts = createAsyncThunk("posts/fetchPosts", async () => {
    try {
      const response = await  axios.get(getPostsUrl, {
        headers: {
          "X-Requested-With": "XMLHttpRequest", 
        },
      })
    
      return response.data
    } catch(error) {
      throw new Error(`Error: ${error.message}`)
    }
  })
  
  export default fetchPosts