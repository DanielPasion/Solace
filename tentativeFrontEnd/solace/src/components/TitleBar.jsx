import React from 'react';
import './TitleBar.css'




const TitleBar = (Props) => {
    return(
        <div className="bar">
            <img id="logo" src={require("./img/Solace-Logo.png")} alt="here lies a logo"></img>
            <img id="title" src={require("./img/Solace-Title.png")} alt="here lies a logo"></img>
            <div id="directions">Directions</div>
        </div>
    );
}

export default TitleBar