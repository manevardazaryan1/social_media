import axios from "axios"
import { createAsyncThunk } from "@reduxjs/toolkit"
import { getCurrentUserUrl } from "../constants/urls"
import { getUsersUrl } from "../constants/urls"

const editProfile = createAsyncThunk("Profile/EditProfile", async ({ userId, profileData }) => {
    try {
        // Update user data (if applicable)

        const userResponse = await axios.patch(`${getUsersUrl}${userId}/`, {
        email: profileData.email, // Update relevant user fields
        username: profileData.username, // Update relevant user fields
        first_name: profileData.first_name, // Update relevant user fields
        last_name: profileData.last_name, // Update relevant user fields
        },  {
                headers: {
                "Content-Type": "multipart/form-data"
            }
        })
        if (!(userResponse.status >= 200 && userResponse.status < 300)) {
            throw new Error("Failed to update user data");
        } 
        
    
        // Update profile data
        const profileResponse = await axios.patch(`${getCurrentUserUrl}${userId}/`, profileData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
    
        if (profileResponse.status >= 200 && profileResponse.status < 300) {
          return profileResponse.data; // Assuming response contains updated profile data
        } else {
          throw new Error("Failed to update profile data");
        }
      } catch (error) {
        throw new Error(`Error: ${error.message}`)
      }
})

export default editProfile