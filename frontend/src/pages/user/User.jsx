import { useEffect, useState } from "react"
import { useParams } from 'react-router-dom'
import "./user.css"
import { useSelector } from 'react-redux'
import { Link } from "react-router-dom"
import { decode, encode } from 'base-64';

function User() {
    const { id }  = useParams()
    const userId = decode(id)

    const users = useSelector((state) => state.users.users.results)
    const posts = useSelector(state => state.posts.posts)
    let user, userPosts

    if (users) {
        user = users.find(user => user.id == userId)
    }
    
    if (posts && user) {
        userPosts = posts.filter(post => post.user === user.username) 
    }


    return (
        <div className="posts">
        {
            user &&  (
                <div className="user-detail">
                    <p>{user.username}</p>
                    <p>{user.email}</p>
                    <p>{user.bio}</p>
                    <p>{user.followers_count}</p>
                    <p>{user.followers}</p>
                    <p>{user.following}</p>
                    <p>{user.profile_picture}</p>
                </div>
            )
        }

        {
            userPosts && <div> 
                {
                    userPosts.map((post) => {
                        return <div key={post.id}> 
                            <Link to={`/post/${encode(post.id.toString())}`}>
                                <img src={post.image} className="post-img"/>
                            </Link>
                        </div>
                    })
                }
            </div>
        }
    </div>
    )
}

export default User