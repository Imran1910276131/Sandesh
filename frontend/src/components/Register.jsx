import React, { useState } from 'react'
import { Link,useNavigate } from 'react-router-dom'
import Axios from 'axios'
const Register = () => {
    const [username,setUsername]=useState(null)
    const [password1,setPassword1]=useState(null)
    const [password2,setPassword2]=useState(null)
    const navigate=useNavigate()
    const registernow=()=>{
        if(password1===password2){
            Axios({
                method:'post',
                url:'http://127.0.0.1:8000/register/',
                data:{
                    'username':username,
                    'password':password1
                }
            }).then(response=>{
                alert('User was Created!!')
                console.log(response.data)
                navigate("/login/")
            }).catch(_=>{
                alert("Something went wrong!")
            })
        }else{
            alert("Passwords do not match!!")
        }
    }
  return (
    <div className="container">
        <div className="content-section">
            <fieldset className="form-group">
                <legend className="border-bottom mb-4">Register Now</legend>
                <div>
                    <div className="form-group">
                        <label>Username</label>
                        <input onChange={(e)=>setUsername(e.target.value)} type="text" className="form-control" placeholder="Username" />
                    </div>
                    <div className="form-group">
                        <label >Password</label>
                        <input onChange={(e)=>setPassword1(e.target.value)} type="password"  className="form-control" placeholder="Password" />
                    </div>

                    <div className="form-group">
                        <label>Confirm Password</label>
                        <input onChange={(e)=>setPassword2(e.target.value)} type="password"  className="form-control" placeholder="Password" />
                    </div>
                </div>
            </fieldset>
            <div className="form-group">
                <p className="btn btn-outline-info" onClick={registernow} >Register</p>
            </div>
            <div className="border-top pt-3">
                <small className="text-muted">
                    Have An Account?
                                <Link className="ml-2" to="/">SignIn In Now</Link>
                </small>
            </div>
        </div>
    </div >
  )
}

export default Register