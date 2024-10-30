import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SocialAuthService, SocialUser } from '@abacritt/angularx-social-login';
import { AuthService } from '../_services/auth.service';
import { User } from '../_models/User';
import { CheckboxControlValueAccessor } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  user2: SocialUser | undefined;
  user: User | undefined;
  showAdminBoard = false;
  showFleetBoard = false;
  showWarehouseBoard = false;
  showLogisticsBoard = false;

  constructor(private authService: AuthService, public socialAuthService: SocialAuthService, private router: Router/*, private _oktaStateService: OktaAuthStateService, @Inject(OKTA_AUTH) private _oktaAuth: OktaAuth*/) {
  }

  ngOnInit(): void {
    this.getUser();
  }

  logout(): void {
    this.socialAuthService.signOut();
  }
  getUser() {
    this.socialAuthService.authState.subscribe((user) => {
      this.user2 = user;
      this.authService.logIn(user.email).subscribe(
        data => {
          this.user = data;
          this.checkRole();
        },
        err => {
          console.log("erro");
          this.socialAuthService.signOut();
        }
      );
    });
  }
  checkRole() {
    switch (this.user?.role) {
      case 'Admin':
        this.showAdminBoard = true;
        this.showFleetBoard = true;
        this.showLogisticsBoard = true;
        this.showWarehouseBoard = true;
        break;
      case 'Logistics Manager':
        this.showFleetBoard = true;
        break;
      case 'Fleet Manager':
        this.showLogisticsBoard = true;
        break;
      case 'Warehouse Manager':
        this.showWarehouseBoard = true;
        break;
    }
  }
}
