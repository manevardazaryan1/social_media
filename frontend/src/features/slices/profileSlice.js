import { createSlice } from '@reduxjs/toolkit'
import fetchCurrentUser from '../../service/fetchCurrentUser'
import postProfilePicture from '../../service/postProfilePicture'
import editProfile from '../../service/editProfile'

const initialState = {
    id: null,
    user: null,
    loading: false,
    error: null,
}

export const profileSlice = createSlice({
    name: "Profile/slice",
    initialState,
    reducers: {
        setCurrentUserId: (state, action) => {
            state.id = action.payload.id
        },
    },
    extraReducers: (builder) => {
        builder
        .addCase(fetchCurrentUser.pending, (state) => {
            state.loading = true
            state.error = null
        })
        .addCase(fetchCurrentUser.rejected, (state, action) => {
            state.loading = false
            state.error = action.error || "Error fetching user data"
        })
        .addCase(fetchCurrentUser.fulfilled, (state, action) => {
            state.loading = false
            state.user = action.payload
        })
        .addCase(postProfilePicture.pending, (state) => {
            state.loading = true;
            state.error = null;
        })
        .addCase(postProfilePicture.fulfilled, (state, action) => {
            state.loading = false;
            if (state.user) {
                state.user.profile_picture = action.payload
            }
        })
        .addCase(postProfilePicture.rejected, (state, action) => {
            console.log(action)
            state.loading = false;
            state.error = action.error || "Error updating profile picture"
        })
        .addCase(editProfile.pending, (state) => {
            state.loading = true;
            state.error = null;
        })
        .addCase(editProfile.fulfilled, (state, action) => {
            state.loading = false;
            if (state.user) {
                state.user = {...state.user, ...action.payload}
            }
        })
        .addCase(editProfile.rejected, (state, action) => {
            state.loading = false;
            state.error = action.error || "Error updating profile data"
        })
    }
})

export const { setCurrentUserId, setCurrentUser } = profileSlice.actions
export default profileSlice.reducer