import { useState,useEffect } from 'react';
import './App.css';
import theme from './theme';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import { ThemeProvider } from '@emotion/react';
import { MyProvider } from './Context';
import Dashboard from './components/Dashboard';
import PrivateRoute from './PrivateRoutes';
import Navbar from './components/Navbar';
import Summary from './components/Summary';
import History from './components/History';
import DateSelection from './components/DateSelection';

function App() {

  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <BrowserRouter>
      {localStorage.getItem('access')?<Navbar/> :null}
        <MyProvider>
          <Routes>
            <Route exact path='/' element={<Home />} />
            <Route exact path='/login' element={<Login />} />
            <Route path= '/' element = {<PrivateRoute />}>
              <Route path = '/provider_notes' element = {<Dashboard />} />
              <Route path = '/history' element = {<History />} />
              <Route path = '/summary' element = {<Summary />} />
              <Route path = '/provider_notes/select-dates/:pid/:name/:gender/:age' element = {<DateSelection />} />
            </Route>
          </Routes>
        </MyProvider>
        </BrowserRouter>
      </ThemeProvider>
    </div>
  );
}

export default App;
