import React, { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import axios from 'axios'
import CustomButton from '../CustomMui/CustomButton'
const Notes = () => {
    const location = useLocation()
    const { pid, name, gender, age, selectedDate } = location.state
    const [data, setData] = useState('')
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(true)
    const [showData, setShowData] = useState(false)
    useEffect(() => {
        axios
            .get(`${process.env.REACT_APP_SERVER_URL}/api/summary/${pid}/${selectedDate}`)
            .then((res) => {
                setData(res.data)
                console.log(res.data)
            })
            .catch(err => {
                setError(err.message);
            });
    }, [])
    return (
        <div className='container'>
            <h1>Provider Notes</h1>
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
            <hr />
            {data && showData &&
                <div>
                    {data.notes.length > 0 &&
                        <div className='patient-detail-table-div'>
                            <h2>Notes</h2>
                            <table className='patient-table patient-detail-table' >
                                <thead>
                                    <th>Date</th>
                                    <th>Age Group</th>
                                    <th>Diagnosis Attached</th>
                                    <th>Note Template</th>
                                    <th>Note Type</th>
                                    <th>Procedure Codes</th>
                                    <th>Visit Reason</th>
                                </thead>
                                <tbody>
                                    {data.notes.map((note, index) => (
                                        <tr key={index}>
                                            <td>{(new Date(note.date)).toUTCString()}</td>
                                            <td>{note.age_group_2}</td>
                                            <td>{note.diagnosis_codes}</td>
                                            <td>{note.note_template}</td>
                                            <td>{note.note_type}</td>
                                            <td>{note.procedure_codes}</td>
                                            <td>{note.visit_reason}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    }
                    <hr />
                    {
                        data.diagnosis.length > 0 &&
                        <div className='patient-detail-table-div'>
                            <h2>Diagnosis</h2>
                            <table className='patient-table patient-detail-table' >
                                <thead>
                                    <th>Date/Time</th>
                                    <th>Description</th>
                                    <th>Chronic</th>
                                    <th>ICD 9</th>
                                    <th>ICD 10</th>
                                    <th>Onset</th>
                                    <th>Past/Current</th>
                                    <th>Severity</th>
                                    <th>Status</th>
                                    <th>type</th>
                                    <th>Comments</th>
                                </thead>
                                <tbody>
                                    {data.diagnosis.map((diag, index) => (
                                        <tr key={index}>
                                            <td>{(new Date(diag.date_time)).toUTCString()}</td>
                                            <td>{diag.description}</td>
                                            <td>{diag.chronic}</td>
                                            <td>{diag.icd_9}</td>
                                            <td>{diag.icd_10}</td>
                                            <td>{diag.onset}</td>
                                            <td>{diag.past_current}</td>
                                            <td>{diag.severity}</td>
                                            <td>{diag.status}</td>
                                            <td>{diag.type}</td>
                                            <td>{diag.comments}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    }
                    <hr />
                    {
                        data.orders.length > 0 &&
                        <div className='patient-detail-table-div'>
                            <h2>Orders</h2>
                            <table className='patient-table patient-detail-table' >
                                <thead>
                                    <th>Order No.</th>
                                    <th>Date/Time</th>
                                    <th>Lab Code</th>
                                    <th>Lab Test Desc</th>
                                    <th>Internal Test Comments</th>
                                    <th>CPT</th>
                                    <th>CPT Desc</th>
                                    <th>Radiology Result</th>
                                </thead>
                                <tbody>
                                    {data.orders.map((ord, index) => (
                                        <tr key={index}>
                                            <td>{ord.orderno}</td>
                                            <td>{(new Date(ord.order_date_time)).toUTCString()}</td>
                                            <td>{ord.lab_code}</td>
                                            <td>{ord.lab_test_description}</td>
                                            <td>{ord.internal_test_comments}</td>
                                            <td>{ord.cpt}</td>
                                            <td>{ord.cpt_description}</td>
                                            <td>{ord.radiology_result}</td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    }
                    <hr />
                    {
                        data.orders.length > 0 &&
                        <div className='patient-detail-table-div'>
                            <h2>Results</h2>
                            <table className='patient-table patient-detail-table' >
                                <thead>
                                    <th>Order No.</th>
                                    <th>Date/Time</th>
                                    <th>Lab Code</th>
                                    <th>Lab Result Code</th>
                                    <th>Loinc</th>
                                    <th>Observation</th>
                                    <th>Range</th>
                                    <th>Unit</th>
                                    <th>Result</th>
                                    <th>Test Description</th>
                                    <th>Laboratory</th>
                                    <th>Flag</th>
                                    <th>Latest Result</th>
                                </thead>
                                <tbody>
                                    {data.orders.map((ord, index) => (
                                        ord.results.map((result, index) => (
                                            <tr key={index}>
                                                <td>{result.orderno}</td>
                                                <td>{(new Date(result.result_date_time)).toUTCString()}</td>
                                                <td>{result.lab_code}</td>
                                                <td>{result.lab_result_code}</td>
                                                <td>{result.loinc}</td>
                                                <td>{result.observation}</td>
                                                <td>{result.range}</td>
                                                <td>{result.unit}</td>
                                                <td>{result.result}</td>
                                                <td>{result.test_description}</td>
                                                <td>{result.laboratory}</td>
                                                <td>{result.flag}</td>
                                                <td>{result.latest_result}</td>
                                            </tr>
                                        ))

                                    ))}
                                </tbody>
                            </table>
                        </div>
                    }
                </div>
            }

            <CustomButton variant='contained' onClick={() => { setShowData(!showData) }}>Show Data</CustomButton>
        </div>
    )
}

export default Notes