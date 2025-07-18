import React, { useState } from 'react'
import '../src/todo.css'


const Todo = () => {

    const [todos, setTodos] = useState([
        // { text: '오늘수업 복습', completed: false, key: 1 },
        // { text: '물 2L마시기', completed: false, key: 2 }
    ])
    // 미션 1. todos에 있는 배열로 li태그를 반복 렌더링 해보자 (map)
    //  completed는 의식 x , text만 잘띄어주면

    // 미션 2. 할 일 추가하기
    // 2-1)사용자가 input에 입력한 텍스트를 어딘가에 보관
    const [newTodoText, setNewTodoText] = useState('')

    // 2-2)todos배열에 객체를 추가
    // -text : 2-1 내용 / completed : false / key : 전에 있던 key + 1
    const handleTodoAdd = () => {
        console.log('handTodoAdd 함수 호출 !', newTodoText)
        // console.log('key값', todos[todos.length - 1].key + 1)
        // spread 문법 : 객체의 모든 속성과 값을 펼쳐서 사용하도록 하는 문법
        //  => "지금 있는 그 상태 "를 의미
        setTodos([...todos,
        {
            text: newTodoText,
            completed: false,
            key: todos.length ? todos[todos.length - 1].key + 1 : 1
        }
        ])
        setNewTodoText("")
    }

    // 미션 3. 할 일 삭제하기
    // 3-1) Delete라는 버튼을 눌렀을때 사용자가 누른 "그" 할 일을 삭제
    //  -> key 값을 추출 
    // 3-2) 그 key 값에 해당하는 할일을 찾아서 삭제 (filter)

    // **함수 호출시,
    // -단순 호출 : onClick = {handleTodoDelete}
    // -매개변수를 통해 값 전달 : handleTodoDelete('abc')
    //     onClick = {()=>{ handleTodoDelete('abc) }}
    const handleTodoDelete = (key) => {
        console.log("handleTodoDelete함수 호출", key)
        let filteredTodos = todos.filter(item => item.key !== key)
        console.log('filteredTodos', filteredTodos)
        setTodos(filteredTodos)
    }

    //  - 할일을 삭제하는것과 달리, 객체 안에있는 속성에 대한 값을 변경  : find
    // 미션 4. 할일 완료 / 미완료

    const handleTodoToggle = (key) => {
        console.log("handleTodoToggle 함수 호출", key)

        let targetTodo = todos.find(item => item.key === key)
        console.log('targetTodo', targetTodo)

        if (targetTodo) {
            targetTodo.completed = !targetTodo.completed
            setTodos([...todos])
        }
    }


    return (
        <div className='todo-container'>
            <h1>Todo List</h1>
            <div className='list-container'>
                <ul className='list-item'>
                    {todos.map(item => (
                        <li key={item.key}>
                            <input
                                  onChange={() => { handleTodoToggle(item.key) }}
                                type="checkbox" ></input>
                            <label style={{
                                textDecoration : item.completed ? 'line-through' : 'none'
                            }}>
                                <span className='todo-text'>{item.text}</span>
                            </label>
                            <button onClick={() => {
                                handleTodoDelete(item.key)
                            }}>Delete</button>
                        </li>
                    ))}
                </ul>
                <div>
                    <input
                        value={newTodoText}
                        type="text" onChange={(e) => {
                            setNewTodoText(e.target.value)
                        }} ></input>
                    <button onClick={handleTodoAdd}>Add</button>
                </div>
            </div>
        </div>
    )
}

export default Todo