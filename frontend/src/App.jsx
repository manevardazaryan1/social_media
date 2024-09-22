import { useEffect } from "react"
// import socialMediaBackendiaUrl from "./constants/urls"
import "./App.css"
import Header from "./components/header/Header"
import getToken from "./service/getToken"
import { socialMediaMainUrl } from "./constants/urls"
import { useSelector, useDispatch } from 'react-redux'
import { setCurrentUserId } from "./features/slices/profileSlice"
import fetchPosts from "./service/fetchPosts"
import fetchUsers from "./service/fetchUsers"
import fetchCurrentUser from "./service/fetchCurrentUser"

function App() {
  const userId = useSelector((state) => state.profile.id)
  const dispatch = useDispatch()

  useEffect(() => {
    async function fetchToken() {
      try {
        const data = await getToken()

        if ( data.token && data.user) {
          dispatch(setCurrentUserId({id: data.user}))
          dispatch(fetchUsers())
          dispatch(fetchCurrentUser(data.user))
          dispatch(fetchPosts())
        }
  
        if (!data.token && data.token ) {
          window.location.href = socialMediaMainUrl
        }
      } catch(err) {
        console.log(err)
      }
    }

    fetchToken()
  }, [dispatch]);

  return (
    <>
    {
      userId && <main className="">
        <Header />
      </main>
    }
    </>
  )
}

export default App
