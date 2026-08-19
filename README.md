# SyndProxy private pool

## Current pool

- Alive now: 1465
- Gold now: 420
- HTTP: 548 alive / 88 gold
- HTTPS: 367 alive / 18 gold
- SOCKS4: 264 alive / 155 gold
- SOCKS5: 286 alive / 159 gold

## Historical pool

- Discovered: 131815
- Ever alive: 20857
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
