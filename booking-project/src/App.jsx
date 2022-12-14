import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import AboutPage from "./pages/AboutPage";
import Services from "./pages/Services";
import SignUp from "./pages/SignUp";
import Landing from "./pages/Landing";
import Login from "./pages/Login";
import { Team } from "./pages/Team";
import House from "../src/pages/House";
import Detailpage from '../src/pages/Detailpage'
import Checkout from "./pages/Checkout";
import PaymentMethod from "./pots/Landing/PaymentMethod";
import Confirm from "./pots/Landing/Confirm";
import LandingHero from "./pots/Landing/LandingHero";
import Campus from "./components/Campus";
import Properties from "./components/Properties";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        
        <Route path="/campus" element={<Campus/>} />
        <Route path="/About" element={<AboutPage />} />
        <Route path="/SignUp" element={<SignUp />} />
        <Route path="/Login" element={<Login />} />
  
        <Route path="/Properties/:slug/:id" element={<Properties />} />
        <Route path="/details/:id" element={<Detailpage />} />
        <Route path="/checkout/:id" element={<Checkout/>} />
        <Route path="/Services" element={<Services />} />
      
        {/* <Route path="/payment" element={<PaymentMethod />} />


        {/* <Route path="/payment" element={<PaymentMethod />} />
        
       
       } />
       
        <Route path="Team" element={<Team />} />

        <Route path="/facilities" element={<Landing />} /> */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;
