import { useSelector, useDispatch } from "react-redux"
import "./profile.css"
import { useState } from "react"
// import postProfilePicture from "../../service/postProfilePicture"
import { Link } from 'react-router-dom'
import { encode, decode } from 'base-64'

function Profile() {
    const dispatch = useDispatch()
    const user = useSelector((state) => state.profile.user)
    const posts = useSelector((state) => state.posts.posts)
    const error = useSelector((state) => state.profile.error)
    const createdPosts = posts.filter(post => post.user === user.username)
    const savedPosts = posts.filter(post => post.saved_by.includes(user))
    // const [pictureUploadModal, setPictureUploadModal] = useState(false)
    // const [editProfile, setEditProfile] = useState(false)

    // const openEditProfileModal = () => {
    //     setEditProfile(true)
    // }
    // console.log(user)
    // console.log(error)
    // async function handleImageUpload(event) {
    //     const file = event.target.files[0];
    //     const formData = new FormData();
    //     formData.append('profile_picture', file); 
    //     await dispatch(postProfilePicture({userId: user.user, profile_picture: formData}))
    // }
    return (
        <>
           { user && <div>
            {
                error && error.message
            }
                <p>{ user.username }</p>
                <p>{ user.followers_count }</p>
                <p>{ user.following_count }</p>
                <p>{ user.email }</p>
                <p>{ user.bio }</p>
                {/* <button className="profile-picture-box" onClick={() => setPictureUploadModal(true)}>
                {
                    user.profile_picture && <img src={ user.profile_picture } className="profile-picture"/>
                }

                {
                    !user.profile_picture && <span className="profile-default-picture">{user.username[0].toUpperCase()}</span>
                }
                </button> */}
                {/* <button onClick={() => openEditProfileModal()}>Edit Profile</button> */}
                <Link to="/settings/edit-profile">
                    Edit Profile
                </Link>
                <p>Followed by { user.followers_count }</p>
                {
                    user.followed_by && user.followed_by.map(user => {
                        <div key={user.id}>
                            <p>{ user.username }</p>
                        </div>
                    })
                }

                <p>Following { user.following_count }</p>
                {
                    user.following && user.following.map(user => {
                        <div key={user.id}>
                            <p>{ user.username }</p>
                        </div>
                    })
                }
            
            </div>
        }

        {/* {
            pictureUploadModal && <div className="picture-upload-modal">
                <button onClick={() => setPictureUploadModal(false)}>X</button>
                <input type="file" accept="image/*" onChange={handleImageUpload} />
            </div>
        } */}

        {/* {
            editProfile && <EditProfileModal closeModal={setEditProfile} user={user}/>
        } */}
        </>
    )
}

export default Profile