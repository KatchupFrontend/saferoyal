import React from 'react'
import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import AboutPage from './pages/AboutPage'
import Services from './pages/Services'
import SignUp from './components/register/SignUp'
import SignIn from './components/register/SignIn'
import { AuthContextProvider } from './context/AuthContext'
import Landing from './pages/Landing'
const App = () => {
    return (
    <BrowserRouter> 
    <AuthContextProvider>
    <Routes>
    <Route path='/' element={<Home/>}/>
    <Route path='/About' element={<AboutPage/>}/>
    <Route path='/Services' element={<Services/>}/>
     <Route path='/SignUp' element={<SignUp/>}/>
    <Route path='/register' element={<SignIn/>}/> 
     <Route path='/facilities' 
     element={
      
            <Landing/>}/>
    </Routes> 
       </AuthContextProvider>
   
    </BrowserRouter>
  )
}

export default App

