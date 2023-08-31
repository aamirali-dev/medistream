import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { IconButton, Pagination } from "@mui/material";
import CustomButton from '../CustomMui/CustomButton';
import CustomTextField from '../CustomMui/CustomTextInput';
import SearchIcon from '@mui/icons-material/Search';
import { useNavigate } from 'react-router-dom';



const Dashboard = () => {
    const navigate = useNavigate()
    const [data, setData] = useState('')
    const [error, setError] = useState('')
    const [page,setPage] = useState(1)
    const [searchValue, setSearchValue] = useState('')
    useEffect(() => {
        axios
            .get(`${process.env.REACT_APP_SERVER_URL}/api/patients/`)
            .then((res) => setData(res.data))
            .catch(err => {
                setError(err.message);
            });
    }, [])
    useEffect(()=>{
        axios
            .get(`${process.env.REACT_APP_SERVER_URL}/api/patients/?page=${page}&search=${searchValue}`)
            .then((res) => setData(res.data))
            .catch(err => {
                setError(err.message);
            });
    },[page,searchValue])
    if (data) {
        console.log(data.results.length)
    }
    const handlePageChange = (e,value)=>{
        setPage(value)
    }

const selectPatient = (pid, name, age, gender)=>{
    const body = {"patientid":pid}
    // axios.post(`${process.env.REACT_APP_SERVER_URL}/api/ /`, body)
    //     .then((res) => {
    //         if(res.status == 200){
    //             navigate('/select-dates')
    //         }
    //     })
    //     .catch((err)=>setError(err.message))
        navigate(`/provider_notes/select-dates/${pid}/${name}/${gender}/${age}`)
}




    return (
        <div>
            {!data && <p className='message'>Loading Please wait...</p>}
            {data  ?
                
            <div className='container'>
                    <div className='search-container'>
                        <div className='search-div'>
                        <CustomTextField type = 'text' name = 'search' label = '' fullWidth placeholder = 'Search...' 
                        onChange = {(e)=>{
                            if(e.target.value.length >1){
                                setSearchValue(e.target.value)
                            }
                            else{
                                setSearchValue('')
                            }
                        }}
                        />
                        </div>
                    <p>Please Enter at least two characters to search.</p>
                    </div>
                    {data.results.length != 0 ? <>
                    {!error? <>
                    <table className='patient-table' >
                        <thead>
                            <th>Patient ID</th>
                            <th>Name</th>
                            <th>Gender</th>
                            <th>Age</th>
                            <th></th>
                        </thead>
                        <tbody>
                        {data.results.map((item,index)=>(
                            item.patientid !==0 &&<tr key = {item.patientid}>
                                <td>{item.patientid}</td>
                                <td>{item.patient_first_name}</td>
                                <td>{item.gender}</td>
                                <td>{item.age_in_years}</td>
                                <td><CustomButton variant='contained'
                                sx ={{
                                    fontSize:'16px',
                                    padding:'4px 7px'
                                }}
                                onClick = {()=>{
                                    selectPatient(item.patientid, item.patient_first_name, item.age_in_years, item.gender)
                                }}
                                >Select</CustomButton></td>
                            </tr>
                        ))}
                        </tbody>
                </table>
                <Pagination count={Math.ceil(data.count / 20)} variant="outlined" color="standard" 
                onChange={handlePageChange}
                />
                </>:<p className='error message'>Error Fetching Data.</p>}
                </>:<p>No records found.</p>}
            </div>
            :null}
        </div>
    )
}

export default Dashboard