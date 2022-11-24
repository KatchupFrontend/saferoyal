import React from 'react'
import HLayout from '../components/HLayout'
import Stats from '../components/stats'
import Serv from '../components/Serv'
import Cards from '../components/cards'
import About from '../components/about'
import Find from '../components/Find'
import Campuses from '../components/Campuses'
const Home = () => {
  return (
    <div>
      <HLayout>
       <Stats/>
       <Serv/>
       <Cards/>
       <Campuses/>
      </HLayout>

    </div>
  )
}

export default Home