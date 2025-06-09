import React from 'react';

function Movie(props) {
  return (
    <div className='bg-white text-black max-w-40 m-2 max-h-70 p-1 rounded justify-between border-2 border-black hover:bg-green-600 hover:text-white'>
      <div className='w-full h-40 bg-gray-800 flex items-center justify-center overflow-hidden'>
        <img
          src={props.poster}
          className='w-full h-full object-cover'
          alt="movie poster"
        />
      </div>
      <div>
        <p className='font-semibold text-sm mt-1'>{props.name}</p>
        <div className='flex justify-between text-xs text-gray-700 mt-1'>
          <p>⭐ {props.rating}</p>
          <p>{props.watched ? "Watched" : "Not Watched"} </p>
        </div>
      </div>
    </div>
  );
}

export default Movie;
