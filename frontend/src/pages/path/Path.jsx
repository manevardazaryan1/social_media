import { useState } from 'react'
import "./path.css"
import { useSelector } from 'react-redux'
import { encode } from 'base-64'
import { Link } from 'react-router-dom'

function Path() {
    const posts = useSelector((state) => state.posts.posts)
    return (
        <>
            <div className="posts">
                {
                    posts && posts.map((post) => {
                        return (
                            <div key={post.id} className="post">
                                <Link to={`/post/${encode(post.id.toString())}`}>
                                    <img src={post.image} className="post-img"/>
                                </Link>
                            </div>
                        )
                    })
                }
            </div>
        </>
    )
}

export default Path