# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 420
- HTTP: 149 alive / 75 gold
- HTTPS: 101 alive / 20 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33851
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
