# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 432
- HTTP: 351 alive / 101 gold
- HTTPS: 291 alive / 30 gold
- SOCKS4: 242 alive / 151 gold
- SOCKS5: 252 alive / 150 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25166
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
