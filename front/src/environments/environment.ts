import { HttpHeaders } from '@angular/common/http';

export const environment = {
  production: false,
  API_URL: 'http://localhost:5000',
  API_HEADERS: {
    headers: new HttpHeaders ({
      'X-API-Key': 'secret',
    }),
    withCredentials: true
  }
};
