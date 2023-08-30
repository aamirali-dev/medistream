import { styled } from '@mui/material/styles';
import {Button} from '@mui/material'
import { useTheme } from '@emotion/react';
import theme from '../theme';
const CustomButton = styled(Button)(({ theme }) => ({
    color: 'white',
    boxShadow:'none',
    margin:'auto',
    fontSize:'20px',
    borderRadius:'0px',
    transition:'background-color 0.6s ease-in-out',
    ":hover":{
        boxShadow:'none',
        color:'white',
        backgroundColor:'black',
        transition:'background-color 0.6s ease-in-out'
    }
    }))

export default CustomButton;