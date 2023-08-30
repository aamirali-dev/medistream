import axios from 'axios';
import { createContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
export const MyContext = createContext("");
const MyProvider = ({ children }) => {
  const navigate = useNavigate()
  const [name, setName] = useState("John Doe");
  const [age, setAge] = useState(1);
  const happyBirthday = () => setAge(age + 1);
  const [loginError, setLoginError] = useState('')
  const [loading,setLoading] = useState(false)

  function sleep(time){
    return new Promise((resolve)=>setTimeout(resolve,time)
  )
}
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
        localStorage.setItem("access",resp.data.access)
        localStorage.setItem("refresh",resp.data.refresh)
        navigate('/provider_notes')
      }
    }
    catch (e) {
      setLoginError(e.response.data.detail)
      console.log(e)
      setLoading(false)
    }
  }
  return (
    <MyContext.Provider value={{ name, age, happyBirthday, login,loginError, loading }}>
      {children}
    </MyContext.Provider>
  );
};

const withUser = (Child) => (props) => (
  <MyContext.Consumer>
    {(context) => <Child {...props} {...context} />}
    {/* Another option is:  {context => <Child {...props} context={context}/>}*/}
  </MyContext.Consumer>
);

export { MyProvider, withUser };