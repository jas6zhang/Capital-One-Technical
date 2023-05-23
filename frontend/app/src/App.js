import "./App.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faShoppingBag } from "@fortawesome/free-solid-svg-icons";
import { faCloudArrowUp } from "@fortawesome/free-solid-svg-icons";
import capone from './capone.png';
import { useState } from "react";

import DataUpload from "./DataUpload";

function App() {
    const [apiResponse, setApiResponse] = useState(null);
    return (
      <div className="App">
        <section>
          <div className="nav">
            <div className="nav-item">
              <h1><FontAwesomeIcon icon={faShoppingBag} id="icon" /> Capital One Rewards Calculator</h1>
            </div>
          </div>
        </section>
        <header className="drop">
          <div className="container">
            <div className="inner">
              <div id="image-box">
                <FontAwesomeIcon icon={faCloudArrowUp} id="upload-icon" />
              </div>
                <DataUpload onApiResponse={setApiResponse} />
            </div>
          </div>
        </header>
        <img src={capone} alt="Logo" className="logo-icon" />
        <div className = "api-response">
          <h2> Your maximum rewards points earned for the month are: </h2>
          {apiResponse ? 
          <div>
            <h3>Points: {apiResponse[0].points} </h3>
            <h3>Rules Applied: {apiResponse[1].rules_used.join(", ")}</h3> 
          </div>
          : null}
        </div> 
      </div> 

    );
  }

export default App;
