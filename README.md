# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 410
- HTTP: 327 alive / 84 gold
- HTTPS: 229 alive / 25 gold
- SOCKS4: 225 alive / 145 gold
- SOCKS5: 267 alive / 156 gold

## Historical pool

- Discovered: 156427
- Ever alive: 29524
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
