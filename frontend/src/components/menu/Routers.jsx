import { BrowserRouter as Router, Route, Routes} from "react-router-dom"
import Path from "../../pages/path/Path"
import Post from "../../pages/post/Post"
import User from "../../pages/user/User"
import Profile from "../../pages/profile/Profile"
import Menu from "./Menu"
import EditProfile from "../../pages/profile/EditProfile"

function Routers() {
    return (
        <>
        <Router>
            <Menu />
            <Routes>
                <Route path="/" element={<Path />} />
                <Route path="/post/:id" element={<Post />} />
                <Route path="/user/:id" element={<User />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="/settings/edit-profile" element={<EditProfile />} />
            </Routes>
        </Router>
        </>
    )
}

export default Routers