# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 394
- HTTP: 140 alive / 81 gold
- HTTPS: 53 alive / 22 gold
- SOCKS4: 158 alive / 138 gold
- SOCKS5: 180 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48026
- Ever gold: 1512

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
