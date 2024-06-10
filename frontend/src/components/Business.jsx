/*eslint-disable*/
import React,{useState,useEffect} from 'react'
import Axios from 'axios'
import SingleNews from './SingleNews'
const Business = () => {
    const[data,setData]=useState(null)
    useEffect (()=>{
        const getdata = async()=>{
            await Axios({
                method:'get',
                url:`http://127.0.0.1:8000/api/tradeview/`
            }).then(response => {
                console.log(response.data)
                setData(response.data)
            })
        }
        getdata()
    },[])
  return (
    <div>
           {
                data !==null ?(
                <>
                    {
                        data.map((d,i)=>(
                            <SingleNews news={d} key={i}/>
                            ))
                    }  
                </>
                ):(<h1>NO Data</h1>)
            }
    </div>
  )
}

export default Business