import React, { useEffect, useState } from 'react';
import Movie from './Movie';
import axios from 'axios'
function Popular() {
  const [movies, setMovies]=  useState([]);


  useEffect(()=>{
    axios.get()
  })

  return (
    <>
      <div>
        <h1>Trending Movies</h1>
        <div className='flex flex-row flex-wrap'>
          {
            movies.map((_, i) => (
              <Movie />
            ))
          }
        </div>
      </div>
    </>
  );
}

export default Popular;
