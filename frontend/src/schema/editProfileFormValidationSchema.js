import * as Yup from 'yup'

export const validationSchema = Yup.object().shape({
    firstName: Yup.string()
    .max(50, 'First name must be 50 characters or less')
    .min(2, "First name must be at least 2 characters"),
    lastName: Yup.string()
    .max(50, 'Last name must be 50 characters or less')
    .min(2, "Last name must be at least 2 characters"), 
    bio: Yup.string().max(500, 'Bio must be 500 characters or less'),
    email: Yup.string().email('Invalid email address').required('Required'),
    username: Yup.string()
    .required('Username is required')
    .min(2, "Username must be at least 2 characters"),
});