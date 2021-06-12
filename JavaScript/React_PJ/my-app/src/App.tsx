import React, { useState } from 'react'
import logo from './logo.svg';
import './App.css';
import TaskInput from './components/TaskInput'
import TaskList from './components/TaskList'
import Task from './components/Types'


const initialState: Task[] = [
  {
    id:2,
    title: '次にやるやつ',
    done: false
  },
  {
    id: 1,
    title: 'はじめにやるやつ',
    done: true
  }
]

const App: React.FC = () => {
  const [tasks, setTasks] = useState(initialState)

  return(
    <div>
      <TaskInput setTasks={setTasks} tasks={tasks} />
      <TaskList setTasks={setTasks} tasks={tasks} />
    </div>
  )

}

export default App;
