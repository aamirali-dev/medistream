import React from 'react';
import {Outlet, Navigate} from 'react-router-dom'
const PrivateRoutes  = ()  =>{
    const token = localStorage.getItem('access')
    return (
        token ?<Outlet /> : <Navigate to='/login' />  
    ) 
}
export default PrivateRoutes;