import React from 'react'
import '../styles/Home.css'
import logo from '../assets/images/logo.png'
import { useNavigate } from 'react-router-dom'
const Home = () => {
    const navigate = useNavigate()
    return (
        <div className='home-container'>
            <div className='logo'>
                <img src  = {logo} className='logo' />
            </div>
            <div className='home-content'>
                <h1 className='home-title'>
                Streamlining Clinical Documentation.
                </h1>
                <p className='home-description'>
                    Clinical documentation is pivotal in healthcare, yet the weight of administrative tasks burdens providers. Our groundbreaking system, powered by ChatGPT, transforms this landscape. 
                </p>
            </div>
            <div className='home-buttons-container'>
                <button className='home-button' onClick = {()=>{navigate('/login')}}>Login</button>
                <button className='home-button'>Ask Help</button>
            </div>
        </div>
    )
}

export default Home