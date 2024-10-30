import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../_services/auth.service';
import { User } from 'src/app/_models/User';
import { Location } from '@angular/common';
import { Router } from '@angular/router';
import { UserRegister } from 'src/app/_models/UserRegister';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  form: any = {
    name: null,
    email: null,
    password: null

  };
  isRegistering =true;
  isSuccessful = true;
  isSignUpFailed = false;
  errorMessage = '';
  isRegistrationFormVisible=false;
  showRegistration=false;
  registrationAttempted = false; 

   
  constructor(private authService: AuthService,private location: Location,private router: Router) { }

  ngOnInit(): void {
    console.log("register component ngoninit")
  }

  onSubmitClient(): void {
    this.registrationAttempted = true; 

    const { name, email,password,} = this.form;
    console.log(name)
    console.log(email)
    console.log(password)
    let user : UserRegister;
    user = this.form;
    this.errorMessage='';
    this.authService.register(user).subscribe(
      data => {
        console.log(data);
        this.isSuccessful = true;
        this.isSignUpFailed = false;
        this.errorMessage =    "Utilizador criado com sucesso.";
        this.authService.setNewUserEmail(email)
        this.router.navigate(['/favorite-genres']);
      },
      (err) => {
        if (err.status === 402) {
          this.errorMessage = 'O e-mail ou o número de telemóvel já estão associados a uma conta existente.';
        } else {
          this.errorMessage = 'Ocorreu um erro durante o registo. Tente novamente mais tarde.';
        }
        this.isSuccessful = false;

        setTimeout(() => {
          console.log("nelson")
          this.isSuccessful==null;
        }, 5000);

        this.isSignUpFailed = true;
      }
    );
  }
  showRegistrationForm() {
    // Mostrar o formulário de registro definindo isRegistrationFormVisible como true
    this.showRegistration = true;
    
  }
  hideRegistrationForm() {
    this.showRegistration = false;
  }
  goBack() {
    //this.location.back();
    this.location.go('/');
    location.reload();

  }
}
