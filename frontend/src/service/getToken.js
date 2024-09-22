import axios from "axios"
import { getTokenUrl } from "../constants/urls"

async function getToken() {

  try {
    const response = await  axios.get(getTokenUrl, {
      headers: {
        "X-Requested-With": "XMLHttpRequest", 
      },
    })
    
    return response.data
  } catch(error) {
    throw new Error(`Error: ${error.message}`)
  }
}

export default getToken