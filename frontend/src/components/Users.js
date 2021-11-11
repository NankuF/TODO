import React from "react";

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.username}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Username</th>
            </tr>
            </thead>
            <tbody>
            {users.map((user) => <UserItem key={user.id} user={user}/>)}
            </tbody>
        </table>
    )
}

export default UserList;