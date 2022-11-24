import React from "react";
import { Link } from "react-router-dom";
import pic6 from '../assets/images/rooms/pic01.jpg'

export default function Login() {
  return (
    <div className="w-full h-screen flex">
      <div className="grid grid-cols-1 md:grid-cols-2 m-auto h-[550px] shadow-lg shadow-gray-600 sm:max-w-[900px]">
        <div className="w-full h-[550px] hidden md:block">
          <img className="w-full h-full" src={pic6} alt="/" />
        </div>
        <div className="p-4 flex flex-col justify-around">
          <form>
            <h2 className="text-4xl font-bold text-center mb-8">SafeRoyal.</h2>
            <div>
              <label htmlFor="">Email</label>
              <input
                className="border p-2 mr-2 mb-5"
                type="text"
                placeholder="Please enter your email"
              />
              <label htmlFor="" className="">
                Password
              </label>
              <input
                className="border p-2 "
                type="password"
                placeholder="Password"
              />
            </div>
            <button className="w-full py-2 my-4 text-white bg-blue-600 hover:bg-blue-500">
              <Link to={'/Landing'}> Sign In</Link>
            </button>
            <p className="text-center">Forgot Username or Password?</p>
          </form>
          <div className="flex items-center ml-4">
            <p>Already have an account?</p>
            <Link to="/SignUp">
              <p className=" text-blue-500 hover:text-blue-600 p-2">Sign up</p>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
