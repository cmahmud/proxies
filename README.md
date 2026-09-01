# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 403
- HTTP: 74 alive / 50 gold
- HTTPS: 40 alive / 21 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47108
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
