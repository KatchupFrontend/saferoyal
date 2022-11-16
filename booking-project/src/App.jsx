import React from 'react'
import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import AboutPage from './pages/AboutPage'
import Services from './pages/Services'
import SignUp from './pages/SignUp'
import Landing from './pages/Landing'
import Login from './pages/Login'
const App = () => {
    return (
    <BrowserRouter> 
  
    <Routes>
    <Route path='/' element={<Home/>}/>
    <Route path='/About' element={<AboutPage/>}/>
    <Route path='/Services' element={<Services/>}/>
    <Route path='/SignUp' element={<SignUp/>}/>
    <Route path='/Login' element={<Login/>}/>
     
     <Route path='/facilities' 
     element={
      
            <Landing/>}/>
    </Routes> 

    </BrowserRouter>
  )
}

export default App

