/*eslint-disable*/
import React, { useState } from 'react';
import { useStateValue } from '../state/StateProvider';

const Profile = () => {
    const [{ profile }, dispatch] = useStateValue();
    const [firstname, setFirstname] = useState(profile?.user?.first_name || '');
    const [lastname, setLastname] = useState(profile?.user?.last_name || '');
    const [email, setEmail] = useState(profile?.user?.email || '');
    const [selectedImage, setSelectedImage] = useState(null);

    const imageonchange = (e) => {
        setSelectedImage(e.target.files[0]);
    };

    const uploadimage = () => {
        if (!selectedImage) {
            alert('Please select an image to upload');
            return;
        }

        const formData = new FormData();
        formData.append('profile_image', selectedImage);

        fetch('http://127.0.0.1:8000/profile/', {
            method: 'POST',
            headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`,
            },
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                if (data.message === 'Image uploaded successfully') {
                    alert('Image uploaded successfully');
                    dispatch({
                        type: 'UPDATE_PROFILE_IMAGE',
                        payload: data.image_url,
                    });
                } else {
                    alert('Image upload failed');
                }
            })
            .catch(error => {
                console.error('Error uploading image:', error);
                alert('Image upload failed');
            });
    };

    const updatedata = async () => {
        const updatedProfile = {
            first_name: firstname,
            last_name: lastname,
            email: email,
        };
    
        try {
            const response = await fetch('http://127.0.0.1:8000/profile/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${localStorage.getItem('token')}`,
                },
                body: JSON.stringify(updatedProfile),
            });
    
            const data = await response.json();
    
            if (data.message === 'Profile updated successfully') {
                alert('Profile updated successfully');
                dispatch({
                    type: 'UPDATE_PROFILE',
                    payload: updatedProfile,
                });
            } else {
                alert('Profile update failed');
            }
        } catch (error) {
            console.error('Error updating profile:', error);
            alert('Profile update failed');
        }
    };
    return (
        <div className="container">
            <div>
                <div className="content-section">
                    <div className="media">
                        <img className="rounded-circle account-img" src={`http://127.0.0.1:8000${profile?.image}`} alt="Profile" />
                        <div className="media-body">
                            <h2 className="account-heading">{profile?.user?.username}</h2>
                            {/* <small className="form-text text-muted">Username name is Fixed</small> */}
                            <p className="text-secondary">{profile?.user?.email}</p>
                            <p>{profile?.user?.first_name} {profile?.user?.last_name}</p>
                        </div>
                    </div>
                    <form method="POST" encType="multipart/form-data">
                        <fieldset className="form-group">
                            <legend className="border-bottom mb-4">Profile Info</legend>
                            <div className="form-group">
                                <label>Upload Profile Picture</label>
                                <div className="row">
                                    <div className="col">
                                        <input onChange={imageonchange} type="file" className="form-control" />
                                    </div>
                                    <div className="col">
                                        <p onClick={uploadimage} className="btn btn-info">Upload</p>
                                    </div>
                                </div>
                            </div>
                            <div className="form-group">
                                <label>First Name</label>
                                <input type="text" className="form-control" onChange={(e) => setFirstname(e.target.value)} value={firstname} />
                            </div>
                            <div className="form-group">
                                <label>Last Name</label>
                                <input type="text" className="form-control" onChange={(e) => setLastname(e.target.value)} value={lastname} />
                            </div>
                            <div className="form-group">
                                <label>Email</label>
                                <input type="email" className="form-control" onChange={(e) => setEmail(e.target.value)} value={email} />
                            </div>
                        </fieldset>
                        <div className="form-group">
                            <p className="btn btn-outline-info" onClick={updatedata}>Update</p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default Profile;
