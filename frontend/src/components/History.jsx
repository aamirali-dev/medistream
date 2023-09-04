import React, {useEffect, useState} from 'react'
import axios from 'axios'
import CustomButton from '../CustomMui/CustomButton'
const History = () => {
    const [data, setData] = useState()
    const [error, setError] = useState()
    useEffect(() => {
        const config = {
            "headers": {
                "Authorization": `JWT ${localStorage.getItem('access')}`
            }
        }
        axios
            .get(`${process.env.REACT_APP_SERVER_URL}/prompts/`, config)
            .then((res) => setData(res.data))
            .catch(err => {
                setError(err.message);
            });
    }, [])
    return (
        <div>
            {data && <div>
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
                                <td>{item.patient_id}</td>
                                <td>{item.patient_first_name}</td>
                                <td>{item.gender}</td>
                                <td>{item.age_in_years}</td>
                                <td><CustomButton variant='contained'
                                sx ={{
                                    fontSize:'16px',
                                    padding:'4px 7px'
                                }}
                                onClick = {()=>{
                                    // selectPatient(item.patient_id, item.patient_first_name, item.age_in_years, item.gender)
                                }}
                                >Select</CustomButton></td>
                            </tr>
                        ))}
                        </tbody>
                </table>
                </div>}
        </div>
    )
}

export default History