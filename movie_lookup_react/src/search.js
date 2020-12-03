import React from "react";
import MovieListing from "./movie_listing.js";


export default class MovieLookup extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            loaded: false,
            movies: {},
            movie_ids: '',
        }

        this.handleSubmit = this.handleSubmit.bind(this)
        this.handleChange = this.handleChange.bind(this)
    }

    async handleSubmit(event) {
        event.preventDefault();

        const req_options = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({movie: this.state.value})
        };

        const response = await fetch('/search_movie', req_options)
            .catch(error => {
                console.log(error)
            }) 
        const data = await response.json();
        this.setState({movies: data, loaded: true})
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    render () {
        return (
            <div className="lookup">
                <form onSubmit={this.handleSubmit}>
                    <input type="text" id='url' value={this.state.value} onChange={this.handleChange}></input>
                    <button type="submit" className="button">Search</button>
                </form>
                {this.state.loaded ?
                    <div>
                        {this.state.movies['data'].map(movie => (
                            <MovieListing movie = {movie} />
                        ))}
                    </div>
                : <h4>Type in a movie, show or series name for more information about it</h4>}
            </div>
        );
    }
}