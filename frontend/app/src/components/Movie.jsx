import React from 'react';

function Movie(props) {
  return (
    <div className='bg-white w-50 h-60 text-black  m-2 max-h-70 p-1 rounded justify-between border-2 border-black hover:bg-green-600 hover:text-white'>
      <div className=' w-full h-40 bg-gray-800 flex items-center justify-center overflow-hidden'>
        <img
          src={props.poster}
          className='w-full h-full object-cover rounded '
          alt="movie poster"
        />
      </div>
      <div>
        <p className='font-semibold text-sm h-4  p-1 m-1' >{props.name? props.name : 'movie name'}</p>
        <div className='flex justify-between  h-4  p-1 m-1'>
          <p>⭐ {props.rating}</p>
          <p>{props.watched ? "Watched" : "Not Watched"} </p>
        </div>
      </div>
    </div>
  );
}

export default Movie;
