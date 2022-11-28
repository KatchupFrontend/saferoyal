import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import { useParams } from "react-router-dom";

const Detailpage = () => {
  const [property, setProperty] = useState();
  const { id } = useParams();
  

    useEffect(() => {
      fetch("http://localhost:8000/api/rooms/")
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          console.log(data);
          setProperty(data);
        });
    }, []);

 
  

  return (
    <div>
    {id}
    
      </div>
  );
};

export default Detailpage;
