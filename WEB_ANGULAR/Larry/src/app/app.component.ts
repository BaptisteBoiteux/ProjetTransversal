import { Component } from '@angular/core';
import { HistRdeComponent } from './hist-rde/hist-rde.component';
import { HistoriqueComponent } from './historique/historique.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {
  title = 'Larry';
  connected = new Boolean(true);
  
  ngOnInit(): void{
  }

  switchconnected(){
    this.connected = !this.connected;
  }
}
