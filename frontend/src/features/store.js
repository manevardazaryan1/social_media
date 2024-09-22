import { configureStore } from '@reduxjs/toolkit'
import profileReducer from './slices/profileSlice'
import postsReducer from './slices/postsSlice'
import usersReducer from './slices/usersSlice'

export const store = configureStore({
    reducer: {
        profile: profileReducer,
        posts: postsReducer,
        users: usersReducer,
    }
  })