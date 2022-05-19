import { Component } from '@angular/core';
import { HistoriqueComponent } from './historique/historique.component';
import { ConnexionComponent } from './connexion/connexion.component'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {
  private title = 'Larry';
  private name= 'Léo';
  private connected = new Boolean(false);

  ngOnInit(): void{
  }

  switchconnected(){
    this.connected = !this.connected;
  }

  setName(name:string) {
    this.name = name;
  }

  getName(){
    return this.name;
  }

  getConnected(){
    return this.connected;
  }

  setConnected(){
    this.connected = !this.connected
  }
}
