# SyndProxy private pool

## Current pool

- Alive now: 1221
- Gold now: 406
- HTTP: 481 alive / 96 gold
- HTTPS: 279 alive / 25 gold
- SOCKS4: 219 alive / 140 gold
- SOCKS5: 242 alive / 145 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31735
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
