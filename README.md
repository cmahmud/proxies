# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 419
- HTTP: 85 alive / 67 gold
- HTTPS: 88 alive / 27 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47263
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
