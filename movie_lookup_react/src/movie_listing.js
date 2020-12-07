import React from 'react';
import './movie_listing.css';
import Rating from './rating.js';

function MovieListing(props) {
    return (
        <div className='movie'>
                <h4>{props.movie['title']}</h4>
                <h5 className='description'>Description: {props.movie['description']}</h5>
                <h5>Released: {props.movie['release_date']}</h5>

                <h5>Directors:</h5>
                <div className='directors'>
                    {props.movie['directors'].map(name => (
                        <li>{name}</li>
                    ))}
                </div>

                <Rating imdb_id={props.movie['imdb_id']}/>
        </div>
    );
}

export default MovieListing;