import React from 'react'



const Footer = () => {
  return (
    <div>
     <footer class="text-gray-400 bg-gray-900 body-font ">
        <hr />
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-wrap md:text-left text-center order-first">
      
      <div class=" md:w-1/2  px-4">
        <h2 class="title-font font-medium text-white tracking-widest text-sm mb-3">APPARTMENTS</h2>
        <nav class="list-none mb-10">
          <li>
            <a class="text-gray-400 hover:text-white">Hotels</a>
          </li>
          <li>
            <a class="text-gray-400 hover:text-white">Hostels</a>
          </li>
          <li>
            <a class="text-gray-400 hover:text-white">Homestels</a>
          </li>
          <li>
            <a class="text-gray-400 hover:text-white">Guest House</a>
          </li>
        </nav>
      </div>
      <div class=" md:w-1/2  px-4">
        <h2 class="title-font font-medium text-white tracking-widest text-sm mb-3">SERVICES</h2>
        <nav class="list-none mb-10">
          <li>
            <a class="text-gray-400 hover:text-white">Easy Booking</a>
          </li>
          <li>
            <a class="text-gray-400 hover:text-white">Affordable pricing</a>
          </li>
          <li>
            <a class="text-gray-400 hover:text-white">Reliable</a>
          </li>
          <li>
            <a class="text-gray-400 hover:text-white">Secured appartments</a>
          </li>
        </nav>
      </div>
     
    </div>
  </div>
  <div class="bg-gray-800 bg-opacity-75 pb-3">
    <div class="container  px-3 flex items-center sm:flex-row flex-col">
      <a class="flex title-font font-medium items-center md:justify-start justify-center text-white">
      <img src="./log.png" alt=""className='' height={80} width={80}/>
        <span class="ml-3 text-xl">OPION</span>
      </a>
      <p class="text-sm text-gray-400 sm:ml-6 sm:mt-0 mt-4">© 2022 —
        <a href="/" class="text-gray-500 ml-1" target="_blank" rel="noopener noreferrer">@OPION</a>
      </p>
      <span class="inline-flex sm:ml-auto sm:mt-0 mt-4 justify-center sm:justify-start">
        <a class="text-gray-400">
          <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-400">
          <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-400">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect>
            <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37zm1.5-4.87h.01"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-400">
          <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" class="w-5 h-5" viewBox="0 0 24 24">
            <path stroke="none" d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"></path>
            <circle cx="4" cy="4" r="2" stroke="none"></circle>
          </svg>
        </a>
      </span>
    </div>
  </div>
</footer>
    
    </div>
  )
}

export default Footer