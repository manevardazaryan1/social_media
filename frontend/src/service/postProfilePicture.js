import axios from "axios"
import { createAsyncThunk } from "@reduxjs/toolkit"
import { getCurrentUserUrl } from "../constants/urls"

const postProfilePicture = createAsyncThunk("Profile/PostProfilePicture", async ({ userId, profile_picture }) => {
    try {
        const response = await axios.patch(`${getCurrentUserUrl}${userId}/`, profile_picture, {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        })

        if (response.status >= 200 && response.status < 300) {
            return response.data.profile_picture
        } else {
            throw new Error(`Failed to update profile picture: ${response.status}`)
        }
    } catch (error) {
        throw new Error(`Error: ${error.message}`)
    }
})

export default postProfilePicture