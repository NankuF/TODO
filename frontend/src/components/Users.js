import React from "react";

const UserItem = ({user}) => {
    return (

        <tr>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.username}
            </td>
        </tr>

    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>
                Firstname
            </th>
            <th>
                Lastname
            </th>
            <th>
                Username
            </th>
            {users.map((user) => <UserItem user={user}/>)}
         </table>
    )
}

export default UserList;