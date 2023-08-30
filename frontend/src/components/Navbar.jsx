import React, { useEffect, useState } from 'react'
import logo from '../assets/images/logo.png'
import { Box, Avatar, IconButton, Tooltip } from '@mui/material'
import { Link, useNavigate } from 'react-router-dom'
const Navbar = () => {
    const navigate = useNavigate()
    const [page, setPage] = useState('')
    useEffect(() => {
        setPage(window.location.href.split('/')[3])
    })

    const handleClick = (page_title) => {
        setPage(page_title)
        navigate(`/${page_title}`)
    }
    return (
        <nav>
            <img src={logo} />
            <div className='tabs'>
                <ul>
                    <li className={page == 'history' ? 'active' : ''}><button to='/history' onClick={() => { handleClick('history') }}>History</button></li>
                    <li className={page == 'provider_notes' ? 'active' : ''}><button to='/provider_notes' onClick={() => { handleClick('provider_notes') }}>Provider Notes</button></li>
        
                </ul>
            </div>
            <Box>
                <IconButton>
                    <Avatar alt='Muhammad' src='' />
                </IconButton>
            </Box>
        </nav>
    )
}

export default Navbar