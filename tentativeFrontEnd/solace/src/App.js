import './App.css';
import TitleBar from './components/TitleBar.jsx';
import TextBox from './components/TextBox.jsx';

function App() {
  return (<>
    <div class="title-bar">
      <TitleBar></TitleBar>
    </div>
    <div class="second-row">
      <div id = "text-box"><TextBox></TextBox></div>
      <img id="solace" src={require("./components/img/Neutral.png")}></img>
    </div>
    </>
  );
}

export default App;
