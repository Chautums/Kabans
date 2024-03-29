import ColorBox from './components/colorBox.ts/colorBox.js'

import './App.css';
import { useState } from 'react';

const defaulCarObject = {
  name: "Audi RS6 C7",
  imageUrl: "https://wheelfront.com/wp-content/uploads/formidable/8/46148653654_7224660e4a_k.jpg",
  description: "Audi revealed the details of the RS 6 Avant on December 5, 2012.[25] Its twin-turbo 4.0 L (3,993 cc) TFSI V8 engine develops 412 kW (560 PS; 553 bhp) at 5700-6600 rpm and 700 N⋅m (516 lbf⋅ft) of torque at 1750-5500 rpm.[26] This will enable the RS 6 Avant to accelerate from 0 to 100 km/h (62.1 mph) in 3.9 seconds.The top speed is limited to 250 km/h (155.3 mph) by default. By adding the optional Dynamic or Dynamic Plus package, this top speed is increased to respectively 280 km/h (174.0 mph) or 305 km/h (189.5 mph).  Audi claims an average fuel consumption of 9.6 L/100 km (29.4 mpg‑imp; 24.5 mpg‑US)[26] and CO2 emissions of 223 g/km.[26] In order to accomplish this, Audi has added a start-stop system and a cylinder on demand system. The RS 6 Avant is offered with an 8-speed tiptronic",
  inStock: false ,
  isLuxus: true , 
  color: [
    {
    name: "Tomato Red",
    colorCode: "C34A2C"
    },

    {
      name: "Panther Black",
      colorCode: "#0f0d0d"
    },

    {
      name: "Nardo Grey",
      colorCode:"#686A6C"
    },

    {
      name: 'Merlin Purple',
      colorCode: '#3e3445'
    },


  ]

}

function App() {
  const [carObject, setCarObject] = useState(defaulCarObject)
  const [newColorValue, setNewColorValue] = useState({
    name: '',
    colorCode: ''
  })

  return (
    <div>
      <div className="car">
        <h1 
          className='car__title'
          onClick={() => {
            const updatedCarObject = {
              ...carObject,
              isLuxus: !carObject.isLuxus
            }


            setCarObject(updatedCarObject)
         }}
        >
          {carObject.name}
          {carObject.isLuxus && (
            <span className='car__star'>
              ⭐️
            </span>
          )}
        </h1>
        <img 
          src={carObject.imageUrl}
          alt="Audi r8" 
          className='car__image'
        />
        <p className='car__info'>
          {carObject.description}
        </p>
        <div className='car__stock-wrapper'>
          <button onClick={() => {
            const updatedCarObject = {
              ...carObject,
              inStock: !carObject.inStock
            }

             setCarObject(updatedCarObject)
          }}>
            Change
          </button>
          <span className={carObject.inStock ? "car__stock" : "car__not-in-stock"}>
            {carObject.inStock ? "In stock" : "Not in stock"}
          </span>
        </div>

        <h4 className="car__title2">
          Available colors
        </h4>
        <div className="car__colors">
          {carObject.color.map((color) => {
              return (
                <ColorBox
                  key={Math.random()}
                  colorName={color.name}
                  colorCode={color.colorCode} 
                />
              )
            })}
        </div>
        <div className="car__form">
          <label className='car__form-label'>
            Color name
            <input 
              type="text" 
              placeholder='Tomato red...'
              value={newColorValue.name}
              onChange={(eventObject) => {
                const updatedNewColorValue = {
                  ...newColorValue,
                  name: eventObject.target.value
                }
    

                setNewColorValue(updatedNewColorValue)
              }}
             />
          </label>
          <label className='car__form-label'>
            Color
            <input 
              type="color"
              value={newColorValue.colorCode}
              onChange={(eventObject) => {
                const updatedNewColorValue = {
                  ...newColorValue,
                  colorCode: eventObject.target.value
                }

                setNewColorValue(updatedNewColorValue)
              }}
             />
          </label>
          <button 
            onClick={() => {
              const updatedCarObject = {
                ...carObject,
                color: [
                  ...carObject.color,
                  { 
                    name: newColorValue.name,
                    colorCode: newColorValue.colorCode
                   }
                ]
              }

              setCarObject(updatedCarObject)

              setNewColorValue({
                name: '',
                colorCode: ''
              })
            }}
            disabled={!newColorValue.name || !newColorValue.colorCode}
          >
            Add color
          </button>
        </div>
      </div>
    </div>
  );
}


export default App;