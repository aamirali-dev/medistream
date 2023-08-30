import { createTheme } from '@mui/material/styles';

const theme = createTheme({
    palette: {
        primary: {
        main: '#10a37f',
        },
        secondary:{
            main:"#3F4144"
        }
    },
    typography: {
        fontFamily:'Poppins'
    }
    });

export default theme