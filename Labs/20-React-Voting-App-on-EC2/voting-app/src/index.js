import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//CODE13: import the VoteApp class to provide the full VoteApp feature
import VoteApp from './components/VoteApp';

//CODE14: call the ReactDOM.render to render out the VoteApp component into the <div id="root"> element within the index.hmtl file
ReactDOM.render(<VoteApp />, document.getElementById('root'));