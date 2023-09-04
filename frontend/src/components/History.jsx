import React, {useEffect, useState} from 'react'
import axios from 'axios'
import CustomButton from '../CustomMui/CustomButton'
import jwtDecode from 'jwt-decode'
import { useNavigate } from 'react-router-dom'
const History = () => {
    const [data, setData] = useState()
    const [error, setError] = useState()
    const {user_id} = jwtDecode(localStorage.getItem('access'))
    const navigate = useNavigate()

    useEffect(() => {
        const config = {
            "headers": {
                "Authorization": `JWT ${localStorage.getItem('access')}`
            }
        }
        axios
            .get(`${process.env.REACT_APP_SERVER_URL}/prompts/${user_id}`, config)
            .then((res) => setData(res.data))
            .catch(err => {
                setError(err.message);
            });
    }, [])
    return (
        <div className='container'>
            <h1>History</h1>
            {data && 
                <table className='patient-table  history-table' >
                        <thead>
                            <th>Sr No.</th>
                            <th>Patient ID</th>
                            <th>Record Date</th>
                            <th>Date Generated</th>
                            <th></th>
                        </thead>
                        <tbody>
                        {data.results.map((item,index)=>(
                            item.patientid !==0 &&<tr key = {item.id}>
                                <td>{item.id}</td>
                                <td>{item.patient_id}</td>
                                <td>{item.date}</td>
                                <td>{(new Date(item.date_created)).toUTCString()}</td>
                                <td><CustomButton variant='contained'
                                sx ={{
                                    fontSize:'16px',
                                    padding:'4px 7px'
                                }}
                                onClick = {()=>{
                                    navigate('/history/view-note', {state:{item}})
                                }}
                                >View</CustomButton></td>
                            </tr>
                        ))}
                        </tbody>
                </table>}
        </div>
    )
}

export default History