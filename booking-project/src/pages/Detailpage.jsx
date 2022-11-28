import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import { useParams } from "react-router-dom";

const Detailpage = () => {
  const [room, setRooms] = useState([]);
  const { id } = useParams();

 const [property, setProperty] = useState();

 useEffect(() => {
   fetch("http://localhost:8000/api/room/" + id)
     .then((res) => {
       return res.json();
     })
     .then((data) => {
       console.log(data);
       setProperty(data);
     });
 }, []);

  console.log(property);
  return <div>
    <h1>Detailpage{id}</h1>
  
  
    

  </div>;
};

export default Detailpage;
