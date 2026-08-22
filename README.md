# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 375
- HTTP: 322 alive / 80 gold
- HTTPS: 286 alive / 25 gold
- SOCKS4: 187 alive / 125 gold
- SOCKS5: 219 alive / 145 gold

## Historical pool

- Discovered: 165812
- Ever alive: 32314
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
