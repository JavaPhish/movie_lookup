import React from 'react';
import './movie_listing.css';

function MovieListing(props) {
    return (
        <div className='movie'>
                <h4>{props.movie['title']}</h4>
                <h5>Description: {props.movie['description']}</h5>
                <h5>Released: {props.movie['release_date']}</h5>
                <h5>Directors:</h5>
                {props.movie['directors'].map(name => (
                    <li>{name}</li>
                ))}
                
        </div>
    );
}

export default MovieListing;