import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import Axios from 'axios'
const Login = () => {
    const[username,setUsername]=useState(null)
    const[password,setPassword]=useState(null)
    console.log(username,password)
    const loginnow=async()=>{
        await Axios({
            method:"post",
            url:"http://127.0.0.1:8000/login/",
            data:{
                'username':username,
                'password':password
            }
        }).then(response=>{
            console.log(response.data,"###Log in page")
            window.localStorage.setItem("token",response.data['token'])
            // console.log(response.data['token'])
            window.location.href="/home"
        }).catch(_=>{
            alert("Your username or password is Invalid")
        })
    }
  return (
    <div className="container">
        <div className="content-section">
            <fieldset className="form-group">
                <legend className="border-bottom mb-4">Log In</legend>
                <div>
                    <div className="form-group">
                        <label >Username</label>
                        <input type="text" onChange={(e)=>setUsername(e.target.value)} className="form-control" placeholder="Username" />
                    </div>
                    <div className="form-group">
                        <label >Password</label>
                        <input  className="form-control" onChange={(e)=>setPassword(e.target.value)} placeholder="Password" />
                    </div>
                </div>
            </fieldset>
            <div className="form-group">
                <p className="btn btn-outline-info" onClick={loginnow} >Login</p>
            </div>
            <div className="border-top pt-3">
                <small className="text-muted">
                    Need An Account?
                    <Link className="ml-2" to="/register/">SignIn Up Now</Link>
                </small>
            </div>
        </div>
    </div >
  )
}

export default Login