# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 422
- HTTP: 148 alive / 76 gold
- HTTPS: 100 alive / 20 gold
- SOCKS4: 185 alive / 160 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33851
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
