# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 408
- HTTP: 78 alive / 55 gold
- HTTPS: 46 alive / 21 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47108
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
