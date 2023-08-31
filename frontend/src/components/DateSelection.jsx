import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom'
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material'
import axios from 'axios'
import CustomButton from '../CustomMui/CustomButton'




const DateSelection = () => {
    const { pid, name, gender, age } = useParams()
    console.log({ pid, name, gender, age })
    const [selectedDate, setSelectedDate] = React.useState('');
    const [dates, setDates] = useState('')
    const [error,setError] = useState('')
    useEffect(() => {
        axios
            .get(`${process.env.REACT_APP_SERVER_URL}/api/dates/${pid}`)
            .then((res) => setDates(res.data))
            .catch(err => {
                setError(err.message);
            });
    }, [])
    const handleChange = (event) => {
        setSelectedDate(event.target.value);
    };
    return (
        <div className='container'>
            <h1>Select Visit Date</h1>
            <table className='patient-table' >
                <thead>
                    <th>Patient ID</th>
                    <th>Name</th>
                    <th>Gender</th>
                    <th>Age</th>
                </thead>
                <tbody>
                    <tr>
                        <td>{pid}</td>
                        <td>{name}</td>
                        <td>{gender}</td>
                        <td>{age}</td>
                    </tr>
                </tbody>
            </table>
            {dates?<div className='select-input'>
                <p>Please select visit date for notes and summary:</p>
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Date:</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={selectedDate}
                    label="Age"
                    onChange={handleChange}
                >
                    {dates.map((date,index)=>(
                        <MenuItem value={date.date} key  = {index}>{(new Date(date.date)).toUTCString()}</MenuItem>
                    ))}
                    
                </Select>
            </FormControl>
            </div>:<p className='select-input'>Please Wait...</p>}
            <CustomButton variant = 'contained'>Continue</CustomButton>
        </div>
    )
}

export default DateSelection