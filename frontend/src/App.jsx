/*eslint-disable*/
import React,{useEffect} from 'react'
import Axios from 'axios'
import { BrowserRouter,Routes,Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './components/Home'
import Profile from './components/Profile'
import { useStateValue } from './state/StateProvider'
import Login from './components/Login'
import Register from './components/Register'
import Sport from './components/Sport'
import World from './components/World'
import Business from './components/Business'
const App=()=> {
  const[{profile},dispatch]=useStateValue()

  useEffect(() => {
    const getProfile = async () => {
      const token = window.localStorage.getItem("token");
      if (token) {
        try {
          const response = await Axios.get('http://127.0.0.1:8000/profile/', {
            headers: {
              Authorization: `token ${token}`
            }
          });
          console.log(response.data);
          dispatch({
            type: "ADD_PROFILE",
            value: response.data['userdata']
          });
        } catch (error) {
          console.error("Error fetching profile:", error);
          dispatch({
            type: 'ADD_PROFILE',
            value: null
          });
        }
      } else {
        dispatch({
          type: 'ADD_PROFILE',
          value: null
        });
      }
    };
  
    getProfile();
  }, [dispatch]);
  return (
    <BrowserRouter>
         <Navbar />
         <Routes>
             
             
             {
              profile!==null ?
              <>
                 <Route exact path='/profile' element={<Profile />} />
                 <Route exact path='/:id/' element={<Home />} />
                 <Route exact path='/sports/' element={<Sport />} />
                 <Route exact path='/world/' element={<World />} />
                 <Route exact path='/business/' element={<Business />} />
              </>
              :
              <>
                 <Route exact path='/login' element={<Login />} />
                 <Route exact path='/register' element={<Register />} />
                 {/* <Route exact path='/:id/' element={<Home />} /> */}
              </>
             }
         </Routes>
    </BrowserRouter>
  )
}
export default App
