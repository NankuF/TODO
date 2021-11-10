import React from "react";
import logo from './logo.svg';
import './App.css';
import UserList from "./components/Users";
import axios from "axios";
import MenuList from "./components/Menu";
import MenuItem from "./components/Menu";
import FooterItem from "./components/Footer";
import ProjectList from "./components/Projects";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users').then(
            response => {
                const users = response.data
                this.setState(
                    {'users': users}
                )
            }
        ).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/projects/').then(
            response => {
                const projects = response.data
                console.log(projects)
                this.setState(
                    {'projects': projects}
                )
                console.log(this.state)
            }
        ).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <MenuItem/>
                <UserList users={this.state.users}/>
                <ProjectList projects={this.state.projects}/>
                <FooterItem/>
            </div>

        )
    }
}

export default App;