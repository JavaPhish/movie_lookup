import React from "react";
import './movie_listing.css';

export default class Rating extends React.Component {
	constructor(props) {
	    super(props);
	    this.state = {
		  likes: 'Loading...',
		  dislikes: 'Loading...',
		  liked: false,
		  disliked: false
	    }
  
	    // the like functions lose context so i have to bind them in order to access state variables
	    this.like = this.like.bind(this)
	    this.dislike = this.dislike.bind(this)
	}

	async like(event) {
		event.preventDefault();

		// Increases like count by one if the user has not already liked (liked: false)
		if (!this.state.liked) {

			this.setState({liked: true});

			const req_options = {
				method: 'POST',
				headers: { 'Content-Type': 'application/json'},
				body: JSON.stringify({imdb_id: this.props.imdb_id})
			  };
		
			const response = await fetch('/like', req_options)
				.catch(error => {
				    console.log(error)
				})
	
			// Update the states data render can update the html with the correct like count
			const data = await response.json();
			this.setState({likes: data['likes']})
			this.setState({dislikes: data['dislikes']})

			console.log("Counted like, thank you!");
		} else {
			this.setState({liked: true});
			console.log("You have already liked this movie! Vote ignored");
		}
	}

	async dislike(event) {
		event.preventDefault();
		// Increases Dislike count by one if the user has not already disliked (disliked: false)

		if (!this.state.disliked) {
			this.setState({disliked: true});

			const req_options = {
				method: 'POST',
				headers: { 'Content-Type': 'application/json'},
				body: JSON.stringify({imdb_id: this.props.imdb_id})
			  };
		
			const response = await fetch('/dislike', req_options)
				.catch(error => {
				    console.log(error)
				})
	
			// Update the states data render can update the html with the correct like count
			const data = await response.json();
			this.setState({likes: data['likes']})
			this.setState({dislikes: data['dislikes']})

			console.log("Counted dislike, thank you!");
		} else {
			console.log("You have already disliked this movie! Vote ignored");
		}
	}

	async componentDidMount(){
		/*
		 * First fetch all the current likes/dislikes from database.
		 * This is run when this specific component is loaded
		 */
		const req_options = {
			method: 'POST',
			headers: { 'Content-Type': 'application/json'},
			body: JSON.stringify({imdb_id: this.props.imdb_id})
		  };
      
            const response = await fetch('/ratings', req_options)
                  .catch(error => {
                      console.log(error)
			})

		// Update the states data render can update the html with the correct like count
		const data = await response.json();
		this.setState({likes: data['likes']})
		this.setState({dislikes: data['dislikes']})
	}


	render () {
	    return (

		  <div className="userRatings">
			<h5>What did you think of {this.props.title}?</h5>
                  <div className="rating">
				<form onSubmit={this.like}>
					<button type="submit" className="like_button">Like ({this.state.likes})</button>
				</form>
				<form onSubmit={this.dislike}>
					<button type="submit" className="dislike_button">Dislike ({this.state.dislikes})</button>
				</form>
                  </div>
		  </div>
	    );
	}
  }