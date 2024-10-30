import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-board-employee',
  templateUrl: './board-employee.component.html',
  styleUrls: ['./board-employee.component.css']
})
export class BoardEmployeeComponent {
  constructor(private router: Router) {}

  registerEmployee() {
    // Redirecionar para a página de registro de funcionários
    this.router.navigate(['/register-employee']);
  }

  viewReservations() {
    // Redirecionar para a página de visualização de reservas
    this.router.navigate(['/reservations']);
  }
  
  disableEmployee(){
    this.router.navigate(['/disable-employee'])
  }
}
