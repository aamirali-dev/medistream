import React, { useContext, useEffect, useState } from 'react'
import logo from '../assets/images/logo.png'
import { Box, Avatar, IconButton, Menu, Typography, MenuItem, } from '@mui/material'
import { Link, useNavigate } from 'react-router-dom'
import { MyContext } from '../Context'

const Navbar = () => {
    const {isAuthenticated} = useContext(MyContext)
    console.log(isAuthenticated)
    const {logout}  = useContext(MyContext)
    const [anchorElUser, setAnchorElUser] = React.useState(null);
    const handleOpenUserMenu = (event) => {
        setAnchorElUser(event.currentTarget);
    };

    const handleCloseUserMenu = () => {
        setAnchorElUser(null);
    };
    const navigate = useNavigate()
    const [page, setPage] = useState('')
    useEffect(() => {
        setPage(window.location.href.split('/')[3])
    })

    const handleClick = (page_title) => {
        setPage(page_title)
        navigate(`/${page_title}`)
    }
    if (!isAuthenticated)
        return 

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
                <IconButton
                    size="large"
                    aria-label="account of current user"
                    aria-controls="menu-appbar"
                    aria-haspopup="true"
                    onClick={handleOpenUserMenu}
                    color="inherit"
                >
                    <Avatar alt='Muhammad' src='' />
                </IconButton>
                <Menu
                    sx={{ mt: '45px', padding: '50px 10px' }}
                    id="menu-appbar"
                    anchorEl={anchorElUser}
                    anchorOrigin={{
                        vertical: 'top',
                        horizontal: 'right',
                    }}
                    keepMounted
                    transformOrigin={{
                        vertical: 'top',
                        horizontal: 'right',
                    }}
                    open={Boolean(anchorElUser)}
                    onClose={handleCloseUserMenu}
                >
                    <MenuItem key={page} onClick={()=>{logout()}}>
                        <Typography textAlign="center" >Logout</Typography>
                    </MenuItem>
                </Menu>
            </Box>
        </nav>
    )
}

export default Navbar