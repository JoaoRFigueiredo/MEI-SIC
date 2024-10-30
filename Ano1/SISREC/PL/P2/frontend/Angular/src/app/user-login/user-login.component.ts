import { Component } from '@angular/core';
import { AuthService } from '../_services/auth.service';
import { Route } from '@angular/router';
import { Router } from '@angular/router';
import { AppComponent } from '../app.component';


@Component({
  selector: 'app-user-login',
  templateUrl: './user-login.component.html',
  styleUrls: ['./user-login.component.css']
})
export class UserLoginComponent {
  email: string = '';
  password: string = '';
  loginerror: string= 'Erro ao fazer login';
  loginError:boolean= false;
  errorMessage = '';
  isSuccessful: boolean | null = null;
  registrationAttempted:boolean=false;
  constructor(private authService: AuthService, private appcomponent: AppComponent, private router: Router) { }

  onSubmit(): void {
    this.registrationAttempted = true;

    console.log('Email:', this.email);
    console.log('Password:', this.password);
    this.authService.logIn(this.email, this.password).subscribe(
      (isLoggedIn: boolean) => {
        if (this.authService.isLoggedIn) {
          console.log("is Logged In")
          this.appcomponent.loggedIn=true;
          this.isSuccessful = true;

          this.authService.setUserEmail(this.email)
          this.loginError=true;
          this.router.navigate(['/personalized-recommendations']);
        } else {
          console.log("is Not Logged In")
          console.error('O login falhou');
          this.errorMessage = 'Ocorreu um erro durante o login. Tente novamente mais tarde.';
          this.isSuccessful = false;
          this.registrationAttempted = false; // Reset after the login attempt
          setTimeout(() => {
            console.log("nelson")
            this.isSuccessful=null;
          }, 3000);
          this.loginError=true;
        }
      },
      (error) => {
        console.error('Erro ao fazer login:', error);
        this.loginError=true;
        console.log(this.loginError)
        this.loginerror = 'Erro ao fazer login'; // Mensagem de erro genérico
        this.errorMessage = 'Ocorreu um erro durante o login. Tente novamente mais tarde.';
        this.isSuccessful = false;
        this.registrationAttempted = false; // Reset after the login attempt
        setTimeout(() => {
          console.log("nelson")
          this.isSuccessful=null;
        }, 3000);
      }
    );
  }
}  