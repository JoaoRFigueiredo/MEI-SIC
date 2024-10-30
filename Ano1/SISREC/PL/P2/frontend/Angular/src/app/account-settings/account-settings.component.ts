import { Component } from '@angular/core';
import { AppointmentService } from '../_services/appointment.service';
import { AuthService } from '../_services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-account-settings',
  templateUrl: './account-settings.component.html',
  styleUrls: ['./account-settings.component.css']
})

export class AccountSettingsComponent {
  constructor(private appointmentService: AppointmentService, private authService: AuthService, private router: Router) { }
  userEmail = this.authService.getUserEmail();
  userName =this.authService.getName();
  
  userPhoneNumber = this.authService.getPhoneNumber();
  
  goBack(){
    this.router.navigate(['/profile'])
  }
}
