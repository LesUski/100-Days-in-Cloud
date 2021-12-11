import React, { Component } from 'react';
//CODE10: import the ProgrammingLanguage class to provide ProgrammingLanguage feature
import ProgrammingLanguage from './ProgrammingLanguage';

class VoteApp extends Component {
  render () {
    //CODE11: provide implementation for the render function to render the HTML for the VoteApp component
    return (
      <main role="main">
        <div class="jumbotron">
          <div class="container">
            <h1 class="display-3">Language Vote App v1</h1>
            &copy; CloudAcademy ❤ DevOps 2019
          </div>
        </div>

        <div class="container">
          <div class="row">
            <div class="col-md-4">
              <ProgrammingLanguage id="go" logo="go.png"/>
            </div>
            <div class="col-md-4">
              <ProgrammingLanguage id="java" logo="java.png"/>
            </div>
            <div class="col-md-4">
              <ProgrammingLanguage id="nodejs" logo="nodejs.png"/>
            </div>
          </div>
        </div>
      </main>
    )
  }
}

//CODE12: export the VoteApp class, allows the ReactDOM.render within the index.js file to use it
export default VoteApp;