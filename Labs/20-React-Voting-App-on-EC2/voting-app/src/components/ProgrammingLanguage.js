import React, { Component } from 'react';
//CODE5: import the Vote class to provide voting feature
import Vote from './Vote';
import axios from 'axios';

class ProgrammingLanguage extends Component {
  constructor () {
    super();

    //CODE6: configure the APIHOSTPORT, this should be the public IP address of the host that the API server is running on
    this.APIHOSTPORT = "localhost:8080";

    this.state = {
      language: {},
      loaded: false
    }
  }

  componentDidMount () {
    //CODE7: provide implementation to request language details for current language from the API server
    axios.get(`http://${this.APIHOSTPORT}/languages/${this.props.id}`).then(
      response => this.setState({
        language: response.data,
        loaded: true
      })
    );
  }

  render () {
    //CODE8: provide implementation for the render function to render the HTML for the ProgrammingLanguage component
    if (this.state.loaded) {
      var usecase = this.state.language.codedetail.usecase;
      var rank = this.state.language.codedetail.rank;
      var homepage = this.state.language.codedetail.homepage;

      return (
        <div class="container">
          <h2>{this.props.name}</h2>
          <p><Vote id={this.props.id}/></p>

          <p><b>Uses</b>: {usecase}</p>
          <p><b>Rank</b>: {rank}</p>
          <p><b>Homepage</b>: {homepage}</p>
          <div class="container">
            <div class="row">
              <div class="col">
                <div class="parent">
                  <img src={"./img/" + this.props.logo} alt="logo" class="center-block"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      )
    }
    return <div></div>;
  }
}

//CODE9: export the ProgrammingLanguage class, allows the VoteApp component to import it
export default ProgrammingLanguage;