import { useState } from 'react'
import './counter.css'

const Counter = () => {
    const [name, setName] = useState(123)
    const [count, setCount] = useState(0)
    const [person, setPerson] = useState({
        name: 'Toms',
        age: 18,
        likeCats: true,
    })

    return (
        <div className='counter'>
            <h2>My name is: {name}</h2>
            <input
             type="text"
             placeholder="Type your name"
             value={name}
             onChange={(eventObject) => {
                setName(eventObject.target.value)
             }}
             />
            <br/><br/><br/>
            <h1>{count}</h1>
            <button onClick={() =>{
                setCount(count + 1)
            }}>
                Add Count
            </button>
            <button
            onClick={() => {
                setCount(count - 1)
            }}>
                Remove count
            </button>
            <button
            onClick={() => {
                setCount(0)
            }}>
                Reset
            </button>
            <br /><br/><br/><br/>
            <h1>Person:</h1>
            <h2>Person name is: {person.name}</h2>
            <h2>Person age is: {person.age}</h2>
            <h2>Person likes cats: {person.likeCats ? "yes" : "no"}</h2>
            <button onClick={()=>{
                setPerson({
                    name:'Ceshka',
                    age: 25,
                    likeCats: person.likeCats,
                })
            }}>
                Change name to Ceshka
            </button>
            <button onClick={() => {
                setPerson({
                    name: person.name,
                    age: person.age +1,
                    likeCats: person.likeCats,
                })
            }}>
                Add +1 to age
            </button>

        </div>
    )
}

export default Counter
