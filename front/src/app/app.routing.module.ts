import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MeetupComponent } from './components/meetup/meetup.component';

const routes: Routes = [
    { path: '', component: MeetupComponent },
    { path: 'meetups/:id', component: MeetupComponent }
  ];
  

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
