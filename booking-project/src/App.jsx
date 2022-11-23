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
import Detailpage from "./pots/Landing/Detailpage";
import Checkout from "./pots/Landing/Checkout";
import PaymentMethod from "./pots/Landing/PaymentMethod";
import Confirm from "./pots/Landing/Confirm";
import LandingHero from "./pots/Landing/LandingHero";
const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/About" element={<AboutPage />} />
        <Route path="/SignUp" element={<SignUp />} />
        <Route path="/Login" element={<Login />} />

        {/* <Route path="/payment" element={<PaymentMethod />} />
        <Route path="/details" element={<Detailpage />} />
        <Route path="/checkout" element={<Checkout />} />
       } />
        <Route path="/Services" element={<Services />} />
         <Route path="/Landing" element={<Landing />} />
        <Route path="Team" element={<Team />} />

        <Route path="/facilities" element={<Landing />} /> */}
      </Routes>
    </BrowserRouter>
  );
};

export default App;
