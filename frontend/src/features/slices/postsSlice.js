import { createSlice } from "@reduxjs/toolkit"
import fetchPosts from "../../service/fetchPosts"

const initialState = {
    loading: false,
    posts: [],
    error: null,
}

export const postsSlice = createSlice({
    name: "Posts/slice",
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
        .addCase(fetchPosts.pending, (state) => {
          state.loading = true
          state.error = null
        })
        .addCase(fetchPosts.fulfilled, (state, action) => {
          state.loading = false
          state.posts = action.payload
        })
        .addCase(fetchPosts.rejected, (state, action) => {
          state.loading = false
          state.error = action.error.message
        });
    }
})

export const { postsActions } = postsSlice.actions
export default postsSlice.reducer
