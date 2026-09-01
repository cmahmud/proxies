# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 403
- HTTP: 72 alive / 50 gold
- HTTPS: 38 alive / 21 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47108
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
