import React from 'react'
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const Properties = () => {
  const [room, setRooms] = useState()
    const {id} = useParams();
    

     useEffect(() => {
       fetch("http://localhost:8000/api/rooms/?category=" +id)
         .then((res) => {
           return res.json();
        })
        .then((data) => {
         console.log(data);
           setRooms(data);
         });
     }, []);

  return (
    <div>
      <p>{id}</p>

      {/* <div class="flex flex-wrap -m-4">
        {room &&
          room.map((item) => (
            <div class="lg:w-1/3 sm:w-1/2 p-4 ">
              <Link to={''}>
                
                    <p>
            
                      {item.apartmentName}
                    </p>
                  
              </Link>
            </div>
          ))}
      </div> */}
    </div>
  );
}

export default Properties