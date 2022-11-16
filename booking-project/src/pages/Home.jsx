import React from 'react'
import Stats from '../components/Home/stats';
import Serv from '../components/Home/Serv'
 import Cards from '../components/Home/cards'
import Footer from '../components/Home/Footer'
import Navbar from '../components/Home/Navbar';
const home = () => {
  return (
    <div>
        <Navbar/>
        <Stats/>
         <Serv/>
        <Cards/>
        <Footer/>  

    </div>
  )
}

export default home