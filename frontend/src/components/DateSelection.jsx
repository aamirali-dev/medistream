import React from 'react'
import { useParams } from 'react-router-dom'
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material'
const DateSelection = () => {
    const { pid, name, gender, age } = useParams()
    console.log({ pid, name, gender, age })
    const [age1, setAge] = React.useState('');

    const handleChange = (event) => {
        setAge(event.target.value);
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
            <div className='select-input'>
                <p>Please select visit for notes and summary:</p>
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Visit Date:</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={age1}
                    label="Age"
                    onChange={handleChange}
                >
                    <MenuItem value={10}>Ten</MenuItem>
                    <MenuItem value={20}>Twenty</MenuItem>
                    <MenuItem value={30}>Thirty</MenuItem>
                </Select>
            </FormControl>
            </div>
        </div>
    )
}

export default DateSelection