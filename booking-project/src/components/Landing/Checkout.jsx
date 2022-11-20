import React from 'react'

const Checkout = () => {
  return (
    <div className="grid h-screen place-items-cente ">
      <div class="   flex   md:py-8   flex-col items-center justify-center  border-3 border-gray-700">
        <div className=" p-4 shadow-2xl">
          <h2 class="text-gray-800 text-lg mb-1 font-medium title-font ">
            
          </h2>
          <p class="leading-relaxed mb-5 text-gray-700">
            Post-ironic portland shabby chic echo park, banjo fashion axe
          </p>
          
            <div class="mb-4">
              <label for="name" class="leading-7 text-sm text-gray-600">
                Full Name
              </label>
              <input
                type="text"
                id="name"
                name="name"
                class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
              />
            </div>
            <div class="relative mb-4">
              <label for="email" class="leading-7 text-sm text-gray-600">
                Email
              </label>
              <input
                type="email"
                id="email"
                name="email"
                class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
              />
            </div>
            <div class="relative mb-4">
              <label for="phone" class="leading-7 text-sm text-gray-600">
                Phone
              </label>
              <input
                type="phone"
                id="email"
                name="email"
                placeholder="Enter your contact number"
                class="w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
              />
            </div>

            <div className="text-center">
              <button className="text-center px-3 py-2 bg-blue-500 w-full text-white">
             Proceed to payment
              </button>
            </div>
          <p class="text-sm text-red-500 mt-3">
            Please these will be required when coming for a room key
          </p>
        </div>
      </div>
    </div>
  );
}

export default Checkout


