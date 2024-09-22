import { Link } from 'react-router-dom'
import "./menu.css"

function Menu() {
    return (
        <>
            <nav >
                <ul >
                    <li >
                        <a href="http://127.0.0.1:8000/user/logout">Logout</a>
                    </li>
                    <li >
                        <Link to={"/profile"}>
                            Profile
                        </Link>
                    </li>
                </ul>
            </nav>
        </>
    )
}

export default Menu