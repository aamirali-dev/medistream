import React from 'react'
import { useLocation } from 'react-router-dom'

const ViewNote = () => {
    const location  = useLocation()
    console.log(location.state)
    return (
        <div className='container'>
            dsfsdfsdf
        </div>
    )
}

export default ViewNote;