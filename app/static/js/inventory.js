// Initialize jQuery Tablesorter on the item table for column sorting
$(document).ready(function() {
    $("#itemTable").tablesorter();

    // Initialize Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Toggle filter row visibility
    $("#toggleFilters").click(function() {
        $(".filter-row").toggle();
        $(this).find('i').toggleClass('bi-funnel bi-funnel-fill');
        // Show/hide the Clear All Filters button based on filter row visibility
        $("#clearFilters").toggle();
    });

    // Show the Clear All Filters button if the filter row is visible on page load
    if ($(".filter-row").is(":visible")) {
        $("#clearFilters").show();
    }
});

// Filter function to dynamically filter table rows based on input values
function filterItems() {
    // Get filter values from inputs
    var filterBarcode = document.getElementById("filterBarcode").value.toLowerCase();
    var filterModel = document.getElementById("filterModel").value.toLowerCase();
    var filterSerial = document.getElementById("filterSerial").value.toLowerCase();
    var filterCondition = document.getElementById("filterCondition").value.toLowerCase();
    var filterAssignedTo = document.getElementById("filterAssignedTo").value.toLowerCase();
    var filterType = document.getElementById("filterType").value.toLowerCase();

    // Loop through each table row and apply filters
    var rows = document.querySelectorAll("#itemTable tbody tr");
    rows.forEach(row => {
        var barcode = row.cells[0].textContent.toLowerCase();
        var model = row.cells[1].textContent.toLowerCase();
        var serial = row.cells[2].textContent.toLowerCase();
        var condition = row.cells[3].textContent.toLowerCase();
        var assignedTo = row.cells[4].textContent.toLowerCase();
        var type = row.cells[5].textContent.toLowerCase();

        // Check if the row matches all filter criteria
        var matchesBarcode = barcode.includes(filterBarcode);
        var matchesModel = model.includes(filterModel);
        var matchesSerial = serial.includes(filterSerial);
        var matchesCondition = filterCondition === "" || condition === filterCondition;
        var matchesAssignedTo = assignedTo.includes(filterAssignedTo);
        var matchesType = filterType === "" || type === filterType;

        // Show or hide the row based on filter matches
        if (matchesBarcode && matchesModel && matchesSerial && matchesCondition && matchesAssignedTo && matchesType) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}

// Clear all filter inputs
function clearFilters() {
    document.getElementById("filterBarcode").value = "";
    document.getElementById("filterModel").value = "";
    document.getElementById("filterSerial").value = "";
    document.getElementById("filterCondition").value = "";
    document.getElementById("filterAssignedTo").value = "";
    document.getElementById("filterType").value = "";
    filterItems(); // Reapply filters to show all rows
}