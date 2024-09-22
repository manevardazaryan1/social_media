import "./profile.css"
import { useState, useEffect } from "react"
import { useSelector, useDispatch } from "react-redux"
import postProfilePicture from "../../service/postProfilePicture"
import { Formik, Form, Field, ErrorMessage  } from 'formik'
import { validationSchema } from "../../schema/editProfileFormValidationSchema"
import editProfile from "../../service/editProfile"

function EditProfile() {
    const dispatch = useDispatch()
    const [pictureUploadModal, setPictureUploadModal] = useState(false)
    const user = useSelector(state => state.profile.user)
    const error = useSelector(state => state.profile.error)
    const users = useSelector(state => state.users.users)
    const [errorMessages, setErrorMessages] = useState({})
    const [resetConfirmationModal, setResetConfirmationModal] = useState(false)
    const [resetFormFunc, setResetFormFunc] = useState(null)
    const [success, setSuccess] = useState(null)

    const handleImageUpload = async (event) => {
        setSuccess(null)
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('profile_picture', file); 
        await dispatch(postProfilePicture({userId: user.user, profile_picture: formData}))
        if (!error) {
            setSuccess("Yor profile has changed successfully!")
        }
        setPictureUploadModal(false)
    }

    const handleResetClick = (resetForm) => {
        setResetFormFunc(() => resetForm)
        setResetConfirmationModal(true)
    }
  
    const confirmReset = () => {
        if (resetFormFunc) resetFormFunc()
        setResetConfirmationModal(false)
    }
  
    const cancelReset = () => {
        setResetConfirmationModal(false)
    }

    const handleSubmit = async (values) => {
        setSuccess(null)
        const {firstName:first_name, lastName:last_name, email, username, bio} = values
        const  profileData = { first_name, last_name, email, username, bio }

        if (users.find(currentUser => currentUser.username === username && currentUser.id != user.user)) {
            setErrorMessages((errorMessages) => ({...errorMessages, usernameError: "Username already taken"}))
        } else {
            setErrorMessages((errorMessages) => ({...errorMessages, usernameError: ""}))
        }

        if (users.find(currentUser => currentUser.email === email && currentUser.id != user.user)) {
            setErrorMessages((errorMessages) => ({...errorMessages, emailError: "Email already taken"}))
        } else {
            setErrorMessages((errorMessages) => ({...errorMessages, emailError: ""}))
        }

        await dispatch(editProfile({ userId: user.user, profileData}))
        if (!error) {
            setSuccess("Yor profile has changed successfully!")
        }
        // console.log("users->user", users.find(user => user.id == user.user))
    } 

    return (
        <>
        {user && <div className="edit-profile-modal">
            <h2>{user.username}</h2>
            <p>Edit profile</p>
            {
                error && <div >{error}</div>
            }
            {
                success && <div >{success}</div>
            }
            <button className="profile-picture-box" onClick={() => setPictureUploadModal(true)}>
                {
                    user.profile_picture && <img src={ user.profile_picture } className="profile-picture"/>
                }

                {
                    !user.profile_picture && <span className="profile-default-picture">{user.username[0].toUpperCase()}</span>
                }
            </button>

            {
                pictureUploadModal && <div className="picture-upload-modal">
                <button onClick={() => setPictureUploadModal(false)}>X</button>
                <input type="file" accept="image/*" onChange={handleImageUpload} />
            </div>
            }

        <Formik
        initialValues={{ firstName: user.first_name, lastName: user.last_name, bio: user.bio, email: user.email, username: user.username }}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
        enableReinitialize={true}
        >
        {({ values, dirty, resetForm }) => (
            <Form>
                {
                    !!Object.values(errorMessages).length && 
                    Object.entries(errorMessages).map(([key, value]) => <div key={key}>{value}</div>)
                }
            <div>
                <label htmlFor="firstName">First Name:</label>
                <Field type="text" name="firstName" placeholder="first name"/>
                <ErrorMessage name="lastName" component="div" />
                
            </div>
            <div>

                <label htmlFor="lastName">Last Name:</label>
                <Field type="text" name="lastName" placeholder="last name" />
                <ErrorMessage name="lastName" component="div" />
            </div> 
            <div>
                <label htmlFor="bio">Bio:</label>
                <Field as="textarea" name="bio" placeholder="bio"/>
                <ErrorMessage name="bio" component="div" />
            </div>
            <div>
                <label htmlFor="username">Username:</label>
                <Field type="text" name="username" placeholder="username" />
                <ErrorMessage name="username" component="div" />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <Field type="email" name="email" placeholder="email"/>
                <ErrorMessage name="email" component="div" />
            </div>
            <button type="submit" disabled={!dirty || !values.email || !values.username }>Edit</button>
            <button type="button" disabled={!dirty} onClick={() => handleResetClick(resetForm)}>Reset</button>
            </Form>
        )}
        </Formik> 
        
        {resetConfirmationModal && (
            <div className="modal">
            <div className="modal-content">
                <h2>Are you sure?</h2>
                <p>Are you sure you want to reset all changes?</p>
                <button onClick={confirmReset}>Yes, Reset</button>
                <button onClick={cancelReset}>Cancel</button>
            </div>
            </div>
        )}
        </div>
        }
        </>
    )
}

export default EditProfile