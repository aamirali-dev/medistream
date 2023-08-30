import { styled } from '@mui/material/styles';
import { TextField } from '@mui/material'
import { useTheme } from '@emotion/react';
import theme from '../theme';
function CustomTextField(props) {
    return (
    <CustomStyled  {...props} fullWidth margin='dense' variant='outlined'
    InputLabelProps={{
        style: { color: '#3F4144' },
        }}
        />
    );
}


const CustomStyled = styled(TextField)(({ theme }) => ({
    color: theme.palette.secondary,
    margin:'20px auto',
    borderRadius: '10px', 
    borderBottom: 'none', 
    outline: 'none',
    }))

export default CustomTextField;