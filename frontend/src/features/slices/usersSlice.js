import { createSlice } from "@reduxjs/toolkit"
import fetchUsers from "../../service/fetchUsers"
import editProfile from "../../service/editProfile"

export const initialState = {
    loading: false,
    error: null,
    users: [],
}

export const usersSlice = createSlice({
    name: "Users/slice",
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
        .addCase(fetchUsers.pending, (state) => {
            state.loading = true
            state.error = null
        })
        .addCase(fetchUsers.rejected, (state, action) => {
            state.loading = false
            state.error = action.error
        })
        .addCase(fetchUsers.fulfilled, (state, action) => {
            state.loading = false
            state.users = action.payload.results
        })
        .addCase(editProfile.pending, (state) => {
            state.loading = true;
            state.error = null;
        })
        .addCase(editProfile.fulfilled, (state, action) => {
            state.loading = false;
            state = JSON.parse(JSON.stringify(state))
            console.log(state)
            const userIndex = state.users.findIndex(user => user.id == action.payload.user)
            if (userIndex) {
                state.users[userIndex] = {...state.users[userIndex], 
                    first_name: action.payload.first_name,
                    last_name: action.payload.last_name,
                    email: action.payload.email,
                    username: action.payload.username
                }
            }
        })
        .addCase(editProfile.rejected, (state, action) => {
            state.loading = false;
            state.error = action.error || "Error updating profile data"
        })
    }
})

export const { userActions } = usersSlice.actions
export default usersSlice.reducer