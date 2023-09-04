import React from 'react'
import CustomButton from '../CustomMui/CustomButton'
import { useNavigate } from 'react-router-dom'

const NotFound = () => {
    const navigate = useNavigate()
  return (
    <div className='not-found'>
        <h1>404 Not Found</h1>
        <h3>The page you are trying to visit does not exists.</h3>
        <div><CustomButton variant='contained' onClick={()=>{navigate('/')}}>Homepage</CustomButton></div>
    </div>
  )
}

export default NotFound