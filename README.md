# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 405
- HTTP: 78 alive / 54 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47108
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
