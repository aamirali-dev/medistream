import React, {useContext, useState} from "react";
import "../styles/Login.css";
import { InputAdornment, IconButton} from '@mui/material'
import { VisibilityOff, Visibility } from "@mui/icons-material";
import CustomButton from "../CustomMui/CustomButton";
import CustomTextField from "../CustomMui/CustomTextInput";
import { MyContext } from "../Context";

const Login = () => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const {login, loginError, loading} = useContext(MyContext)
    const handle_submit = (e) => {
        e.preventDefault()
        login(username, password)
    };
    const [showPassword, setShowPassword] = React.useState(false);

    const handleClickShowPassword = () => setShowPassword((show) => !show);
    
    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };
    return (
    <div className="home-container">
        <div className="login-container">
        <h1 className="page-heading">Login</h1>
        <form onSubmit={handle_submit}>
            <CustomTextField
            label="Username: "
            required
            type="text"
            fullWidth
            onChange = {(e)=>{
                setUsername(e.target.value)
            }}
            />
        <CustomTextField
            label="Password: "
            required
            type={showPassword ? "text" : "password"}
            InputProps={{ // <-- This is where the toggle button is added.
                endAdornment: (
                    <InputAdornment position="end">
                    <IconButton
                        aria-label="toggle password visibility"
                        onClick={handleClickShowPassword}
                        onMouseDown={handleMouseDownPassword}
                    >
                        {!showPassword ? <Visibility /> : <VisibilityOff />}
                    </IconButton>
                    </InputAdornment>
                )
                }}
                onChange = {(e)=>{
                    setPassword(e.target.value)
                }}
        />
        <p className="error">{loginError}</p>
            <CustomButton variant="contained" fullWidth type="submit" disabled= {loading}>
            Login
            </CustomButton>
            <p className = 'forget-passwd'>
            If you forgot password or do not have any account, please contact
            administrators.
            </p>
        </form>
        </div>
    </div>
    );
};

export default Login;
