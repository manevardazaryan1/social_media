import { useParams } from 'react-router-dom'
import { Link } from 'react-router-dom'
import "./post.css"
import { useSelector } from "react-redux"
import { encode, decode } from 'base-64'

function Post() {
    const { id }  = useParams()
    const postId = decode(id)
    const posts = useSelector((state) => state.posts.posts)
    const post = posts.find(post => post.id == postId)
    return (
        <>
            <div className="post">
                {
                    post &&  (
                        <div className="post-detail">
                            <img src={post.image} className="post-detail-img"/>
                            <p>{post.content}</p>
                            <p>{post.created_at.split("T")[0]}</p>
                            <p>{post.likes_count}</p>
                            <Link to={`/user/${encode(post.user_id.toString())}`}>
                                <p>{post.user}</p>
                            </Link>
                            <p>{post.is_liked}</p>
                            <p>{post.comments}</p>
                            <p>{post.liked_by}</p>
                            <p>{post.is_saved}</p>
                        </div>
                    )
                }
            </div>
        </>
    )
}

export default Post