# SyndProxy validated proxy pool

## Current pool

- Alive now: 365
- Gold now: 331
- HTTP: 41 alive / 24 gold
- HTTPS: 3 alive / 1 gold
- SOCKS4: 156 alive / 156 gold
- SOCKS5: 165 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43613
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
