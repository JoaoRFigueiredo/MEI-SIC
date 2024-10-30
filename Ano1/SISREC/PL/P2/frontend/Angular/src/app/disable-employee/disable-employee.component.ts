import { Component } from '@angular/core';
import { AuthService } from '../_services/auth.service';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-disable-employee',
  templateUrl: './disable-employee.component.html',
  styleUrls: ['./disable-employee.component.css']
})
export class DisableEmployeeComponent {
  userEmail: string | null;

  constructor(private userService: AuthService,private location: Location) {
    this.userEmail = this.userService.getUserEmail();
}
 isDeleted: boolean = false;

 confirmDelete(confirm: boolean) {
  if (confirm && this.userEmail !== null) {
    console.log(this.userEmail);
    this.userService.inactive(this.userEmail);
    this.isDeleted = true;
    
    // Aguardar 3 segundos antes de continuar
    setTimeout(() => {
      this.location.go('/');
      location.reload();
    }, 1000);
  }


  if(!confirm){
    this.location.back();
    console.log("user nao quis apagar a conta")
    }
}
}