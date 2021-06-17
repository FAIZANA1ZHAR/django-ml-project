

const  aclen = document.getElementById('aclen');
const  arco  = document.getElementById('arco');
const  novmmg  = document.getElementById('novmmg');
const  tdmin  = document.getElementById('tdmin');
const tablel = document.getElementById("table1");


function checkInputs() {
	// trim to remove the whitespaces
  var validation = true; 
  const aclenValue = aclen.value.trim();
  const  arcoValue  = arco.value.trim();
  const  novmmgValue  = novmmg.value.trim();
  const  tdminValue  = tdmin.value.trim();
  const  tdcalValue  = tdcal.value.trim();
  const  tdchargeValue  =  tdcharge.value.trim();
  const  teveminValue  = tevemin.value.trim();
  const  tevecalValue  = tevecal.value.trim();
  const  tnigchgValue  = tnigchg .value.trim();
  const   tnigcalValue  =  tnigcal.value.trim();
  const  tnigmValue  = tnigm.value.trim();
  const  tevechgValue  = tevechg.value.trim();

  const  cuscalValue  = cuscal.value.trim();
    const    vmplValue  =   vmpl.value.trim();
	const  iplValue  = ipl.value.trim();
	const  ivcalValue  = ivcal.value.trim();


  
  
  
  
  

  

  if(aclenValue < 0 || aclenValue == '' ) {
		setErrorFor(aclen, 'Account lenght invalid');
		validation = false;
	} else {
		setSuccessFor(aclen);
	}
	

	if(arcoValue < 0 || arcoValue  == '') {
		setErrorFor(arco , 'AreaCode cannot be blank');
		validation = false;
	} else {
		setSuccessFor(arco );
	}

	if(novmmgValue < 0 || novmmgValue == '') {
		setErrorFor(novmmg, 'Vmail cannot be blank');
		validation = false;
	} else {
		setSuccessFor(novmmg);
	}


	if( tdminValue< 0 || tdminValue == '' ) {
		setErrorFor(tdmin, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tdmin);
	}



	if(tdcalValue < 0 || tdcalValue == '' ) {
		setErrorFor(tdcal, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tdcal);
	}


	if(tdchargeValue   < 0 || tdchargeValue == '') {
		setErrorFor(tdcharge, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tdcharge);
	}


	if(teveminValue  < 0 || teveminValue == '') {
		setErrorFor(tevemin, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tevemin);
	}

	if( tevecalValue < 0 || tevecalValue == '') {
		setErrorFor(tevecal, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tevecal);
	}



	if(tnigchgValue  < 0 ||  tnigchgValue == '') {
		setErrorFor(tnigchg, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tnigchg);
	}


	if( tnigcalValue < 0 ||  tnigcalValue == '') {
		setErrorFor(tnigcal, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tnigcal);
	}


	if( tnigmValue < 0 ||  tnigmValue == '' ) {
		setErrorFor(tnigm, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tnigm);
	}

	if(tevechgValue  < 0 ||  tevechgValue == '') {
		setErrorFor(tevechg, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(tevechg);
	}


	if( cuscalValue < 0 || cuscalValue == '') {
		setErrorFor(cuscal, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(cuscal);
	}


	if( vmplValue < 0 || vmplValue == '' ) {
		setErrorFor(vmpl, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(vmpl);
	}



	if(  iplValue < 0 ||  iplValue == '') {
		setErrorFor(ipl, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(ipl);
	}

	if( ivcalValue < 0 ||  ivcalValue == '') {
		setErrorFor(ivcal, 'total day mint cannot be blank');
		validation = false;
	} else {
		setSuccessFor(ivcal);
	}



	if (validation == true)
	{
		alert(" GOOD")
		myFunction()

	} else {
		alert("NOT  GOOD")
	}


	

}





function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}


function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}



function myFunction(){

	alert("hiii")
	
	const website = document.getElementById("aclen").value;
	const url = document.getElementById("arco").value;
	tablel.innerHTML += `
	<tr>
	
				 <td>Account length:</td>
				 <td><input type="text" id="aclen" name="Accountlength" ></td>
				 <td>Area code:</td>
				 <td><input type="text" id="arco" name="Areacode" ></td>
			 
				 <td>Number vmail messages:</td>
				 <td><input type="text" id="novmmg" name="Numbervmailmessages" ></td>
				 <td>Total day minutes:</td>
				 <td><input type="text" id="fname" name="Totaldayminutes"  ></td>
				 <td><input type="text" id="fname" name="Totaldayminutes" ></td>
			 
	<td><button id="bt1" class="deleteBtn" >Delete</button></td>
	<td><button id="bt1" class="deleteBtn" >Save</button></td>
 </tr>
   `;
   alert(" GOOD")
   tablel.addEventListener("click", onDeleteRow);
 
 }
 
 function onDeleteRow(e) {
   if (!e.target.classList.contains("deleteBtn")) {
	 return;
   }
 
   const btn = e.target;
   btn.closest("tr").remove();
 }

