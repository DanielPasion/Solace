import React from 'react';
import './TitleBar.css'




const TitleBar = (Props) => {
    return(
        <div className="bar">
            <div id="logo">UrMom</div>
            <div id="sonder">Sonder</div>
            <div id="directions">Directions</div>
        </div>
    );
}

export default TitleBar