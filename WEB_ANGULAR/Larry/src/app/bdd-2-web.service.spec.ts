import { TestBed } from '@angular/core/testing';

import { Bdd2WebService } from './bdd-2-web.service';

describe('Bdd2WebService', () => {
  let service: Bdd2WebService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Bdd2WebService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
