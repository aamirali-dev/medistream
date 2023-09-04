import axios from 'axios';
import { createContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
export const MyContext = createContext("");
const MyProvider = ({ children }) => {
  const navigate = useNavigate()
  const [name, setName] = useState("John Doe");
  const [age, setAge] = useState(1);
  const happyBirthday = () => setAge(age + 1);
  const [loginError, setLoginError] = useState('')
  const [loading, setLoading] = useState(false)
  const [isAuthenticated, setIsAuthenticated] = useState(()=> localStorage.getItem('access') ? true : false)



  const login = async (username, password) => {
    setLoading(true)
    setLoginError('')
    const body = {
      username, password
    }
    try {
      const resp = await axios.post(`${process.env.REACT_APP_SERVER_URL}/auth/jwt/create/`, body)
      if (resp.status == 200) {
        setLoading(false)
        localStorage.setItem("access", resp.data.access)
        localStorage.setItem("refresh", resp.data.refresh)
        navigate('/provider_notes')
        setIsAuthenticated(true)
      }
    }
    catch (e) {
      setLoginError(e.response.data.detail)
      console.log(e)
      setLoading(false)
    }
  }

  const logout = async () => {
    setLoading(true)
    const body = {
      "refresh": localStorage.getItem('refresh')
    }
    try {
      const resp = await axios.post(`${process.env.REACT_APP_SERVER_URL}/auth/logout/`, body)
      if (resp.status == 200) {
        setLoading(false)
        localStorage.removeItem("access")
        localStorage.removeItem("refresh")
        navigate('/login')
        setIsAuthenticated(false)
      }
    }
    catch (e) {
      setLoading(false)
      console.log(e)
    }
  }
  return (
    <MyContext.Provider value={{ name, age, happyBirthday, login, loginError, loading, logout, isAuthenticated }}>
      {children}
    </MyContext.Provider>
  );
};


export { MyProvider };