import React from 'react'
import { useLocation } from 'react-router-dom'

const ViewNote = () => {
    const location  = useLocation()
    const {id,date,date_created, patient_id, prompt} = location.state.item
    return (
        <div className='container'>
            <h1>History</h1>
            <table className='p-details-table'>
                <tbody>
                    <tr>
                        <td className='bold'>Prompt ID:</td>
                        <td>{id}</td>
                    </tr>
                    <tr>
                        <td className='bold'>Patient ID:</td>
                        <td>{patient_id}</td>
                    </tr>
                    <tr>
                        <td className='bold'>Record Date:</td>
                        <td>{(new Date(date)).toUTCString()}</td>
                    </tr>
                    <tr>
                        <td className='bold'>Date Created:</td>
                        <td>{(new Date(date_created)).toUTCString()}</td>
                    </tr>
                </tbody>
            </table>
            <div className='iframe'>
            <iframe srcdoc={prompt} width='100%' height='100%' />
            </div>
        </div>
    )
}

export default ViewNote;