import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MeetupComponent } from './components/meetup/meetup.component';
import { MeetupListComponent } from './components/meetup-list/meetup-list.component';

const routes: Routes = [
    { path: '', component: MeetupListComponent },
    { path: 'meetups', component: MeetupListComponent },
    { path: 'meetups/:id', component: MeetupComponent }
  ];
  

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
