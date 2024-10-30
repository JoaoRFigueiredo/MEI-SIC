import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/_models/User';
import { AuthService } from '../_services/auth.service';
import { Router } from '@angular/router';
import { Location } from '@angular/common';
import {SocialAuthService,SocialUser} from '@abacritt/angularx-social-login';
import { UserRegister } from '../_models/UserRegister';
@Component({
  selector: 'app-register-employee',
  templateUrl: './register-employee.component.html',
  styleUrls: ['./register-employee.component.css']
})
export class RegisterEmployeeComponent implements OnInit {
  form: any = {
    firstName: null,
    phoneNumber: null,
    lastName: null,
    email: null,
    role: null
  };
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';
  isRegistrationFormVisible=false;
  showRegistration=false;
  registrationAttempted = false; 
  title = 'Angular12JwtAuth';
  private roles: string[] = [];
  username?: string;
  user: SocialUser | undefined;
  loggedIn: boolean | undefined;
  isSignInFailed = false;
  isAClient= false;
  isAEmployee=false;
  constructor(private authService: AuthService,public socialAuthService: SocialAuthService,private location: Location,private router: Router) { 
    if (this.isAEmployee) {
      // Navegar para a rota /board-employee
      console.log("is employee")
    }
  }

  ngOnInit(): void {
    console.log("register component ngoninit")
  }

  onSubmitEmployee(): void {
    this.registrationAttempted = true; 
    const { firstName, phoneNumber, lastName, email, role } = this.form;
    this.form.role= "employee"
    console.log("employee registado role é " +this.form.role)
    console.log()
    let user : UserRegister;
    user = this.form;
    this.errorMessage='';
    this.authService.register(user).subscribe(
      data => {
        console.log(data);
        this.isSuccessful = true;
        this.isSignUpFailed = false;
        this.errorMessage = "Utilizador criado com sucesso.";
 
      },  
      (err) => {
        if (err.status === 402) {
          this.errorMessage = 'O e-mail ou o número de telemóvel já estão associados a uma conta existente.';
        } else {
          this.errorMessage = 'Ocorreu um erro durante o registo. Tente novamente mais tarde.';
        }
  
        this.isSignUpFailed = true;
      }
    );
  }
  goBack() {
    this.location.back();

  }
  hideRegistrationForm() {
    this.showRegistration = false;
  }
  verifyLogin() {
    console.log("verify login")
    this.socialAuthService.authState.subscribe((user) => {
      this.user = user;
      console.log("alberto é "+this.loggedIn)
      this.loggedIn = user != null; 
      if (this.loggedIn) {
        console.log(user.email);
       
          
        
    
        console.log("this is client"+this.isAClient)
        this.hideRegistrationForm();
      
      }
      else{
        console.log(this.loggedIn+ "is not loggedin?")
        this.loggedIn=false;
      }
    
    })
  }
isEmployee() {
  console.log("isEmployee acedido");
  if (this.user) {
    this.authService.isEmployee(this.user.email).subscribe((isEmployee) => {
      if (isEmployee) {
        console.log('Usuário é um Employee.');
        this.isAEmployee=true;
        this.router.navigate(['/board-employee']);
      } else {
        this.isAEmployee=false;
        console.log('Usuário não é um Employee.');
      }
    });
  }
}
}