<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Test Report</title>
    <link href="assets/style.css" rel="stylesheet" type="text/css"/></head>
  <body onLoad="init()">
    <script>/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/. */


function toArray(iter) {
    if (iter === null) {
        return null;
    }
    return Array.prototype.slice.call(iter);
}

function find(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return elem.querySelector(selector);
}

function find_all(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return toArray(elem.querySelectorAll(selector));
}

function sort_column(elem) {
    toggle_sort_states(elem);
    var colIndex = toArray(elem.parentNode.childNodes).indexOf(elem);
    var key;
    if (elem.classList.contains('numeric')) {
        key = key_num;
    } else if (elem.classList.contains('result')) {
        key = key_result;
    } else {
        key = key_alpha;
    }
    sort_table(elem, key(colIndex));
}

function show_all_extras() {
    find_all('.col-result').forEach(show_extras);
}

function hide_all_extras() {
    find_all('.col-result').forEach(hide_extras);
}

function show_extras(colresult_elem) {
    var extras = colresult_elem.parentNode.nextElementSibling;
    var expandcollapse = colresult_elem.firstElementChild;
    extras.classList.remove("collapsed");
    expandcollapse.classList.remove("expander");
    expandcollapse.classList.add("collapser");
}

function hide_extras(colresult_elem) {
    var extras = colresult_elem.parentNode.nextElementSibling;
    var expandcollapse = colresult_elem.firstElementChild;
    extras.classList.add("collapsed");
    expandcollapse.classList.remove("collapser");
    expandcollapse.classList.add("expander");
}

function show_filters() {
    var filter_items = document.getElementsByClassName('filter');
    for (var i = 0; i < filter_items.length; i++)
        filter_items[i].hidden = false;
}

function add_collapse() {
    // Add links for show/hide all
    var resulttable = find('table#results-table');
    var showhideall = document.createElement("p");
    showhideall.innerHTML = '<a href="javascript:show_all_extras()">Show all details</a> / ' +
                            '<a href="javascript:hide_all_extras()">Hide all details</a>';
    resulttable.parentElement.insertBefore(showhideall, resulttable);

    // Add show/hide link to each result
    find_all('.col-result').forEach(function(elem) {
        var collapsed = get_query_parameter('collapsed') || 'Passed';
        var extras = elem.parentNode.nextElementSibling;
        var expandcollapse = document.createElement("span");
        if (extras.classList.contains("collapsed")) {
            expandcollapse.classList.add("expander")
        } else if (collapsed.includes(elem.innerHTML)) {
            extras.classList.add("collapsed");
            expandcollapse.classList.add("expander");
        } else {
            expandcollapse.classList.add("collapser");
        }
        elem.appendChild(expandcollapse);

        elem.addEventListener("click", function(event) {
            if (event.currentTarget.parentNode.nextElementSibling.classList.contains("collapsed")) {
                show_extras(event.currentTarget);
            } else {
                hide_extras(event.currentTarget);
            }
        });
    })
}

function get_query_parameter(name) {
    var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}

function init () {
    reset_sort_headers();

    add_collapse();

    show_filters();

    sort_column(find('.initial-sort'));

    find_all('.sortable').forEach(function(elem) {
        elem.addEventListener("click",
                              function(event) {
                                  sort_column(elem);
                              }, false)
    });

};

function sort_table(clicked, key_func) {
    var rows = find_all('.results-table-row');
    var reversed = !clicked.classList.contains('asc');
    var sorted_rows = sort(rows, key_func, reversed);
    /* Whole table is removed here because browsers acts much slower
     * when appending existing elements.
     */
    var thead = document.getElementById("results-table-head");
    document.getElementById('results-table').remove();
    var parent = document.createElement("table");
    parent.id = "results-table";
    parent.appendChild(thead);
    sorted_rows.forEach(function(elem) {
        parent.appendChild(elem);
    });
    document.getElementsByTagName("BODY")[0].appendChild(parent);
}

function sort(items, key_func, reversed) {
    var sort_array = items.map(function(item, i) {
        return [key_func(item), i];
    });

    sort_array.sort(function(a, b) {
        var key_a = a[0];
        var key_b = b[0];

        if (key_a == key_b) return 0;

        if (reversed) {
            return (key_a < key_b ? 1 : -1);
        } else {
            return (key_a > key_b ? 1 : -1);
        }
    });

    return sort_array.map(function(item) {
        var index = item[1];
        return items[index];
    });
}

function key_alpha(col_index) {
    return function(elem) {
        return elem.childNodes[1].childNodes[col_index].firstChild.data.toLowerCase();
    };
}

function key_num(col_index) {
    return function(elem) {
        return parseFloat(elem.childNodes[1].childNodes[col_index].firstChild.data);
    };
}

function key_result(col_index) {
    return function(elem) {
        var strings = ['Error', 'Failed', 'Rerun', 'XFailed', 'XPassed',
                       'Skipped', 'Passed'];
        return strings.indexOf(elem.childNodes[1].childNodes[col_index].firstChild.data);
    };
}

function reset_sort_headers() {
    find_all('.sort-icon').forEach(function(elem) {
        elem.parentNode.removeChild(elem);
    });
    find_all('.sortable').forEach(function(elem) {
        var icon = document.createElement("div");
        icon.className = "sort-icon";
        icon.textContent = "vvv";
        elem.insertBefore(icon, elem.firstChild);
        elem.classList.remove("desc", "active");
        elem.classList.add("asc", "inactive");
    });
}

function toggle_sort_states(elem) {
    //if active, toggle between asc and desc
    if (elem.classList.contains('active')) {
        elem.classList.toggle('asc');
        elem.classList.toggle('desc');
    }

    //if inactive, reset all other functions and add ascending active
    if (elem.classList.contains('inactive')) {
        reset_sort_headers();
        elem.classList.remove('inactive');
        elem.classList.add('active');
    }
}

function is_all_rows_hidden(value) {
  return value.hidden == false;
}

function filter_table(elem) {
    var outcome_att = "data-test-result";
    var outcome = elem.getAttribute(outcome_att);
    class_outcome = outcome + " results-table-row";
    var outcome_rows = document.getElementsByClassName(class_outcome);

    for(var i = 0; i < outcome_rows.length; i++){
        outcome_rows[i].hidden = !elem.checked;
    }

    var rows = find_all('.results-table-row').filter(is_all_rows_hidden);
    var all_rows_hidden = rows.length == 0 ? true : false;
    var not_found_message = document.getElementById("not-found-message");
    not_found_message.hidden = !all_rows_hidden;
}
</script>
    <h1>test_searchCustomer.py</h1>
    <p>Report generated on 18-Sep-2020 at 16:57:35 by <a href="https://pypi.python.org/pypi/pytest-html">pytest-html</a> v2.1.1</p>
    <h2>Environment</h2>
    <table id="environment">
      <tr>
        <td>Module Name</td>
        <td>Account</td></tr>
      <tr>
        <td>Packages</td>
        <td>{"pluggy": "0.13.1", "py": "1.9.0", "pytest": "6.0.1"}</td></tr>
      <tr>
        <td>Platform</td>
        <td>Windows-10-10.0.19041-SP0</td></tr>
      <tr>
        <td>Project Name</td>
        <td>nop commerce</td></tr>
      <tr>
        <td>Python</td>
        <td>3.8.5</td></tr>
      <tr>
        <td>Tester</td>
        <td>Saurabh</td></tr></table>
    <h2>Summary</h2>
    <p>7 tests ran in 75.21 seconds. </p>
    <p class="filter" hidden="true">(Un)check the boxes to filter the results.</p><input checked="true" class="filter" data-test-result="passed" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="passed">7 passed</span>, <input checked="true" class="filter" data-test-result="skipped" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="skipped">0 skipped</span>, <input checked="true" class="filter" data-test-result="failed" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="failed">0 failed</span>, <input checked="true" class="filter" data-test-result="error" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="error">0 errors</span>, <input checked="true" class="filter" data-test-result="xfailed" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="xfailed">0 expected failures</span>, <input checked="true" class="filter" data-test-result="xpassed" disabled="true" hidden="true" name="filter_checkbox" onChange="filter_table(this)" type="checkbox"/><span class="xpassed">0 unexpected passes</span>
    <h2>Results</h2>
    <table id="results-table">
      <thead id="results-table-head">
        <tr>
          <th class="sortable result initial-sort" col="result">Result</th>
          <th class="sortable" col="name">Test</th>
          <th class="sortable numeric" col="duration">Duration</th>
          <th>Links</th></tr>
        <tr hidden="true" id="not-found-message">
          <th colspan="4">No results found. Try to check the filters</th></tr></thead>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">testCases/test_AddCustomer.py::Test_AddCustomer::test_Validate_addCustomer</td>
          <td class="col-duration">14.13</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_AddCustomer.py:20 ********* testcase 3 login*************
[32mINFO    [0m root:test_AddCustomer.py:23 ********* login *************
[32mINFO    [0m root:test_AddCustomer.py:28 ****************** Admin Logged In *************************
[32mINFO    [0m root:test_AddCustomer.py:55 **************** customer has been added successfully. ***************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">testCases/test_AddCustomer.py::Test_AddCustomer::test_Validate_Failing_addCustomer</td>
          <td class="col-duration">13.15</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_AddCustomer.py:64 ********* testcase 4 login*************
[32mINFO    [0m root:test_AddCustomer.py:67 ********* login *************
[32mINFO    [0m root:test_AddCustomer.py:72 ****************** Admin Logged In *************************
[32mINFO    [0m root:test_AddCustomer.py:79 ************ without entering register info click on save
[32mINFO    [0m root:test_AddCustomer.py:86 *********** testcase pass when no info entered and not saving customer *************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">testCases/test_SearchCustomerBy.py::Test_SearchCustomerBy::test_SearchByEmailid</td>
          <td class="col-duration">7.66</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_SearchCustomerBy.py:26 *********launching browser*******
[32mINFO    [0m root:test_SearchCustomerBy.py:33 ********* Logged In *******
[32mINFO    [0m root:test_SearchCustomerBy.py:38 ********* search by email *******<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">testCases/test_login.py::Test_Login::test_homePageTitle</td>
          <td class="col-duration">1.51</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login.py:19  *************** this test case 1 *************** 
[32mINFO    [0m root:test_login.py:20  *************** verifing case 1 *************** 
[32mINFO    [0m root:test_login.py:28  ************************** this test case 1 is pass ************************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">testCases/test_login.py::Test_Login::test_loginPage_Title</td>
          <td class="col-duration">6.58</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login.py:39  ************************** this test case 2 ************************ 
[32mINFO    [0m root:test_login.py:52  ************************** this test case 2 is pass ************************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">testCases/test_login_DDT.py::Test_002_DDT_Login::test_homePageTitle</td>
          <td class="col-duration">1.51</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login_DDT.py:18  *************** this test case 1 *************** 
[32mINFO    [0m root:test_login_DDT.py:19  *************** verifing case 1 *************** 
[32mINFO    [0m root:test_login_DDT.py:27  ************************** this test case 1 is pass ************************<br/></div></td></tr></tbody>
      <tbody class="passed results-table-row">
        <tr>
          <td class="col-result">Passed</td>
          <td class="col-name">testCases/test_login_DDT.py::Test_002_DDT_Login::test_login</td>
          <td class="col-duration">7.38</td>
          <td class="col-links"></td></tr>
        <tr>
          <td class="extra" colspan="4">
            <div class="log"> -------------------------------Captured log call-------------------------------- <br/>[32mINFO    [0m root:test_login_DDT.py:36  ************************** this test case 2 ************************ 
[32mINFO    [0m root:test_login_DDT.py:48  ************************** this test case 2 is pass ************************<br/></div></td></tr></tbody></table></body></html>