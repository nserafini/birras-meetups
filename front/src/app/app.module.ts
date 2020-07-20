import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { MeetupComponent } from './components/meetup/meetup.component';
import { AppRoutingModule } from './app.routing.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module';
import { MeetupListComponent } from './components/meetup-list/meetup-list.component';
import { CookieService } from 'ngx-cookie-service';



@NgModule({
  declarations: [
    AppComponent,
    MeetupComponent,
    MeetupListComponent
  ],
  imports: [
    BrowserModule,   
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule
  ],
  providers: [CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }
