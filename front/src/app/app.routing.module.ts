import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MeetupComponent } from './components/meetup/meetup.component';
import { MeetupListComponent } from './components/meetup-list/meetup-list.component';
import { MeetupCreateComponent } from './components/meetup-create/meetup-create.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
    { path: '', component: MeetupListComponent },
    { path: 'login', component: LoginComponent },
    { path: 'meetup-create', component: MeetupCreateComponent }
  ];
  

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
