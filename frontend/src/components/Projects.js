import React from "react";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>

        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                Project
            </th>

            {
                projects.map((project) => <ProjectItem project={project}/>)
            }

        </table>
    )
}

export default ProjectList;