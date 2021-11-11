import React from "react";
import './App.css';
import UserList from "./components/Users";
import ProjectList from "./components/Projects";
import TodoList from "./components/Todos";
import axios from "axios";
import {BrowserRouter, Route, Link} from 'react-router-dom';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users').then(
            response => {
                const users = response.data.results
                this.setState(
                    {'users': users}
                )
            }
        ).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/projects').then(
            response => {
                const projects = response.data.results
                this.setState(
                    {'projects': projects}
                )
            }
        ).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todo').then(
            response => {
                const todos = response.data.results
                this.setState(
                    {'todos': todos}
                )
            }
        ).catch(error => console.log(error))
    }

    render() {
        return (
            <div className={'App'}>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to={'/'}>Users</Link>
                            </li>
                            <li>
                                <Link to={'/projects'}>Projects</Link>
                            </li>
                            <li>
                                <Link to={'/todos'}>Todos</Link>
                            </li>
                        </ul>
                    </nav>
                    <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todos' component={() => <TodoList todos={this.state.todos}/>}/>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
