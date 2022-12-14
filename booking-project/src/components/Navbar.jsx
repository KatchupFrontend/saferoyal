import React from 'react'
import { BiMenuAltRight } from 'react-icons/bi';
import { FaTimes } from 'react-icons/fa';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import HomeHero from './HomeHero';



const Navbar = () => {
    const [nav,setNav] = useState(false);
    const links = [
        {
            id: 1,
            link: 'home',
            url: '/'
        },
        {  
            id: 2,
            link: 'about',
            url: '/about'
        },
        {
            id: 3,
            link: 'services',
            url: '/services'
        },
        {
            id:4,
            link: 'be a host'
            
        }
    
    ];


  return (
    <div className="hero-image">
      <div className=" h-24 max-w-screen mx-auto z-[100]">
        <div className="flex justify-between items-center h-24  max-w-screen mx-auto px-4 text-white">
          <div className="flex items-center ">
            <h1 className="text-3xl font-bold text-white cursor-pointer">
              Safe<span className='text-blue-500'>Royal</span>
            </h1>
          </div>

          <ul className="hidden md:flex ">
            {links.map(({ id, link, url }) => (
              <li
                key={id}
                className="p-4 capitalize hover:text-blue-500 cursor-pointer duration-300 text-xl"
              >
                <Link to={url}> {link}</Link>
              </li>
            ))}
          </ul>
          <div className=" md:flex hidden">
            <Link to="/Login">
              <button className=" bg-blue-500 rounded-lg px-4 py-2 hover:bg-blue-600 m-4">
                Register
              </button>
            </Link>
            {/* <button className='m-4 py-2 px-3 bg-transparent hover:bg-blue-600 rounded-lg '>Log In</button> */}
          </div>
          <div
            className=" md:hidden cursor-pointer p-3"
            onClick={() => {
              setNav(true);
            }}
          >
            <BiMenuAltRight size={33} className="text-white" />
          </div>
        </div>

        <div
          className={
            nav
              ? "md:hidden fixed left-0 top-0 w-full h-full bg-gray-600/70 backdrop-blur z-40"
              : ""
          }
        >
          <div
            className={
              nav
                ? "shadow-xl fixed left-0 top-0 w-4/5 bg-black z-40 text-white h-full p-10 ease-in duration-300"
                : "fixed top-0 left-[-100%] p-10 duration-300 ease-in h-full z-40 "
            }
          >
            <div className="flex items-center justify-between w-full text-white">
              <img src="./log.png" height={100} width={100} alt="pic" />
             
              <div onClick={() => setNav(false)} className="cursor-pointer p-3">
                <FaTimes size={30} />
              </div>
            </div>
            <ul className="pt-10">
              {links.map(({ id, link, url }) => (
                <li
                  key={id}
                  className="p-4 hover:text-blue-600 duration-300 text-lg cursor-pointer"
                >
                  <Link to={url}>{link}</Link>
                </li>
              ))}
            </ul>
            <div>
              <Link to="/Login">
                <button className=" bg-blue-500 rounded-lg px-4 py-2 hover:bg-blue-600 m-4">
                  Register
                </button>
              </Link>
            </div>
          </div>
        </div>
        <HomeHero/>
      </div>
    </div>
  );
}

export default Navbar


