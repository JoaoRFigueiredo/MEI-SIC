import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './_services/auth.service';
import { User } from 'src/app/_models/User';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  form: any = {
    firstName: null,
    phoneNumber: null,
    lastName: null,
    email: null,
    role: null
  };
  newuserfirstname?: string;
  newuserlastname?: string;
  newuseremail?: string;
  newuserphonenumber?: string;
  newuserrole?: string;
  showRegistration: boolean | undefined;
  title = 'Angular12JwtAuth';
  private roles: string[] = [];
  username?: string;
  user: undefined;
  loggedIn: boolean = false;
  isSignInFailed = false;
  isAClient= false;
  isAEmployee=false;
  constructor(private authService: AuthService,private router: Router) {
   
  this.router.navigate(['/board-client']);
    
  
    if (!this.loggedIn){
      this.router.navigate(['/']);

    }
  
  }

  ngOnInit(): void {
    this.loggedIn =this.authService.isLoggedIn
    console.log("bernardo -> "+this.loggedIn)
    this.router.navigate(['/board-client'])
   
  
    console.log("ngnOnInit app accessed")
    this.hideRegistrationForm(); // Ocultar o formulário de registro
    this.showRegistration = false;
    //this.router.navigate(['/login']);
    const token = localStorage.getItem('token');
    if (token) {
      // Enviar o token para o servidor para verificação
      // Se for válido, o usuário continua autenticado
    }
    this.verifyLogin();
    
  }
  refreshPage(): void {
    location.reload();
  }
  logout(): void {
    //this.socialAuthService.signOut();
  }
  openRegisterForm(){
    console.log("opening register form")
    this.router.navigate(['/register']);
  }
  verifyLogin() {
    console.log("verify login");
  }
  
  
  /*submitRegistrationFormClient() {
    console.log('Primeiro Nome:', this.newuserfirstname);
    console.log('Último Nome:', this.newuserlastname);
    console.log('Email:', this.newuseremail);
    console.log('Número de Telefone:', this.newuserphonenumber);
    this.newuserrole='client';
    const {  newuserfirstname, newuserlastname,newuseremail, newuserphonenumber, newuserrole } = this.form;
    let user : User;
    user = this.form;
    this.authService.register(userRe).subscribe(
      data => {
        console.log(data);        
      },
      err => {
     
      }
    );

  }*/
  
  showRegistrationForm() {
    // Mostrar o formulário de registro definindo isRegistrationFormVisible como true
    this.showRegistration = true;
  }

  hideRegistrationForm() {
    this.showRegistration = false;
  }
}