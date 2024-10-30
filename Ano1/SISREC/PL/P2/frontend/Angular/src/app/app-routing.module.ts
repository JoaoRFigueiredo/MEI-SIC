import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterComponent } from './board-admin/register/register.component';
import { LoginComponent } from './login/login.component';
import { BoardAdminComponent } from './board-admin/board-admin.component';
import { GetUsersComponent } from './board-admin/get-users/get-users.component';
import { BoardClientComponent } from './board-client/board-client.component';
import { TesteComponent } from './teste/teste.component';
import { BoardEmployeeComponent } from './board-employee/board-employee.component';
import { RegisterEmployeeComponent } from './register-employee/register-employee.component';
import { ReservationsComponent } from './reservations/reservations.component';
import { DisableEmployeeComponent } from './disable-employee/disable-employee.component';

import { ExemploestabelecimentoComponent } from './estabelecimentosespecificos/exemploestabelecimento/exemploestabelecimento.component';
import { FavoritosComponent } from './favoritos/favoritos.component';
import { DescriptionExampleComponent } from './Descriptions/description-example/description-example.component';
import { ProfileComponent } from './profile/profile.component';
import { PastRatingsComponent } from './past-ratings/past-ratings.component';
import { FavoriteMoviesComponent } from './favorite-movies/favorite-movies.component';
import { AccountSettingsComponent } from './account-settings/account-settings.component';
import { UserLoginComponent } from './user-login/user-login.component';
import { PersonalizedRecommendationsComponent } from './personalized-recommendations/personalized-recommendations.component';
import { FavoriteGenresComponent } from './favorite-genres/favorite-genres.component';
import { MoviessimilaarPerfilComponent } from './moviessimilaar-perfil/moviessimilaar-perfil.component';
const routes: Routes = [
  //{ path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'users', component: GetUsersComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'admin', component: BoardAdminComponent },
  { path: 'board-client', component: BoardClientComponent },
  { path: 'teste', component: TesteComponent },
  { path: 'board-employee', component: BoardEmployeeComponent },
  { path: 'register-employee', component: RegisterEmployeeComponent },
  { path: 'reservations', component: ReservationsComponent },
  { path: 'disable-employee', component: DisableEmployeeComponent },
  { path: 'favoritos', component: FavoritosComponent },
  { path: 'solario1', component: ExemploestabelecimentoComponent },
  { path: 'description1', component: DescriptionExampleComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'past-ratings', component: PastRatingsComponent },
  { path: 'favorite-movies', component: FavoriteMoviesComponent },
  {path: 'account-settings', component: AccountSettingsComponent},
  {path: 'user-login', component: UserLoginComponent},
  {path: 'personalized-recommendations', component: PersonalizedRecommendationsComponent},
  {path: 'favorite-genres', component: FavoriteGenresComponent},
  {path: 'moviessimilaar-perfil', component: MoviessimilaarPerfilComponent}
  //{ path: 'login/callback', component: OktaCallbackComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
