$(document).ready(function() {
	var name = document.getElementById("id_firm_name");
	var cif = document.getElementById("id_fiscal_id");
	var reg = document.getElementById("id_fiscal_reg");
	var ba = document.getElementById("id_bank_account");
	var bn = document.getElementById("id_bank_name");
	var bill_addr = document.getElementById("id_bill_address");
	if ($('#id_bill').find(":selected").val() == '1') {
		$('#firm').attr("style", "display:none");
		name.value = "bogus";
		cif.value = "RO23406564";
		reg.value = "J31/521/2008";
		ba.value = "RO49AAAA1B31007593840000";
		bn.value = "bogus";
		bill_addr.value = "bogus";
		return;
	}
});

function getValue(sel)
{
	var opm = sel.options[sel.selectedIndex].value;
	var parts = opm.split("_|!|_");
	var name = document.getElementById("id_firm_name");
	var cif = document.getElementById("id_fiscal_id");
	var reg = document.getElementById("id_fiscal_reg");
	var ba = document.getElementById("id_bank_account");
	var bn = document.getElementById("id_bank_name");
	var bill_addr = document.getElementById("id_bill_address");

	if (opm == '1') {
		$('#firm').attr("style", "display:none");
		name.value = "bogus";
		cif.value = "RO23406564";
		reg.value = "J31/521/2008";
		ba.value = "RO49AAAA1B31007593840000";
		bn.value = "bogus";
		bill_addr.value = "bogus";
		return;
	}
	$('#firm').attr("style", "display:block");
	if (opm == '2') {
		name.value = "";
		cif.value = "";
		reg.value = "";
		ba.value = "";
		bn.value = "";
		bill_addr.value = "";
		return;
	}
	name.value = parts[0];
	cif.value = parts[1];
	reg.value = parts[2];
	ba.value = parts[3];
	bn.value = parts[4];
	bill_addr.value = parts[5];
}

