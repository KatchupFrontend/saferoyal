import React from "react";
import { useEffect } from "react";
import { useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Detailpage = () => {
  const [property, setProperty] = useState([]);
  const { id } = useParams();

  const getSingleProperty = async () => {
    const response = await axios.get(`http://localhost:8000/api/room/${id}`);
    const data = await response.json();
    console.log(data);
    setProperty(data);
  };

  useEffect(() => {
    getSingleProperty();
  }, []);

  

    // useEffect(() => {
    //   fetch("http://localhost:8000/api/room/" + id)
    //     .then((res) => {
    //       return res.json();
    //     })
    //     .then((data) => {
    //       console.log(data);
    //       setProperty(data);
    //     });
    // }, []);

 console.log(property);
  

  return (
    <div>
    {id}
      </div>
  );
};

export default Detailpage;
