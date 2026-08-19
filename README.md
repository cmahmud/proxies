# SyndProxy private pool

## Current pool

- Alive now: 1218
- Gold now: 500
- HTTP: 416 alive / 148 gold
- HTTPS: 345 alive / 91 gold
- SOCKS4: 213 alive / 125 gold
- SOCKS5: 244 alive / 136 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17313
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
