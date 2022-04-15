original_table="""<table>
    </td>
        <td>• [auto_reload](#auto_reload) </td>
        <td> ➜ [usage](#-usage) </td>
        <td> ⛭ [technical details](#-technical-details) </td>
    </tr>
    <tr>
        <td>• [debug.Log](#debug.Log) </td>
        <td> ➜ [usage](#-usage-1) </td>
        <td> ⛭ [technical details](#-technical-details-1) </td>
    </tr>
    <tr>
        <td> •  [debug.Timer](#debug.Timer) </td>
        <td> ➜ [usage](#-usage-2) </td>
        <td> ⛭ [technical details](#-technical-details-2) </td>
    </tr>
    <tr>
        <td> •  [extended_list](#extended_list) </td>
        <td> ➜ [usage](#-usage-3) </td>
        <td> ⛭ [technical details](#-technical-details-3) </td>
    </tr>
    <tr>
        <td> •  [files.load_file](#files.load_file) </td>
        <td> ➜ [usage](#-usage-4) </td>
        <td> ⛭ [technical details](#-technical-details-4) </td>
    </tr>
    <tr>
        <td> •  [linked_values](#linked_values) </td>
        <td> ➜ [usage](#-usage-5) </td>
        <td> ⛭ [technical details](#-technical-details-5) </td>
    </tr>
    <tr>
        <td> •  [progress_bar](#progress_bar) </td>
        <td> ➜ [usage](#-usage-6) </td>
        <td> ⛭ [technical details](#-technical-details-6) </td>
    </tr>
    <tr>
        <td> •  [assertion](#assertion) </td>
        <td> ➜ [usage](#-usage-7) </td>
        <td> ⛭ [technical details](#-technical-details-7) </td>
    </tr>
    <tr>
        <td> •  [testing.test](#testing.test) </td>
        <td> ➜ [usage](#-usage-8) </td>
        <td> ⛭ [technical details](#-technical-details-8) </td>
    </tr>
    <tr>
        <td> •  [to_string](#to_string) </td>
        <td> ➜ [usage](#-usage-9) </td>
        <td> ⛭ [technical details](#-technical-details-9) </td>
    </tr>
    <tr>
        <td> •  [constants](#constants) </td>
        <td> ➜ [usage](#-usage-10) </td>
        <td> ⛭ [technical details](#-technical-details-10) </td>
    </tr>
    <tr>
        <td> •  [variables.get_all_subclasses](#variables.get_all_subclasses) </td>
        <td> ➜ [usage](#-usage-11) </td>
        <td> ⛭ [technical details](#-technical-details-11) </td>
    </tr>
    <tr>
        <td> •  [variables.get_instances](#variable.get_instances) </td>
        <td> ➜ [usage](#-usage-12) </td>
        <td> ⛭ [technical details](#-technical-details-12) </td>
    </tr>
    <tr>
        <td> •  [variables.get_names](#variables.get_names) </td>
        <td> ➜ [usage](#-usage-13) </td>
        <td> ⛭ [technical details](#-technical-details-13) </td>
    </tr>
</table>"""

# convert all the [name](#name) syntax to <a href="#name">name</a>


def convert_to_links(table):
    """
    Convert all the [name](#name) syntax to <a href="#name">name</a>
    """
    new_table = ""
    for line in table.split("\n"):
        new_line = line
        if "<td>" in line:
            link = line.split("(")[1].split(")")[0]
            name = line.split("<td>")[1].split("]")[0].replace("[", "")
            new_line = f"        <td><a href=\"{link}\">{name}</a></td>"
        new_table += new_line + "\n"
    return new_table
print(convert_to_links(original_table))