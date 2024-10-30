import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  constructor(private router: Router) {}

  futureAppointments() {
    // Redirecionar para a página de registro de funcionários
    this.router.navigate(['/favorite-movies']);
  }
  pastRatings() {
    // Redirecionar para a página de registro de funcionários
    this.router.navigate(['/past-ratings']);
  }
  accountSettings() {
    // Redirecionar para a página de registro de funcionários
    this.router.navigate(['/account-settings']);
  }
  similarMoviesPerfil() {
    // Redirecionar para a página de registro de funcionários
    this.router.navigate(['/moviessimilaar-perfil']);
  }

}
