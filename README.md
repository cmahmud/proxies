# SyndProxy private pool

## Current pool

- Alive now: 1265
- Gold now: 470
- HTTP: 441 alive / 131 gold
- HTTPS: 346 alive / 75 gold
- SOCKS4: 225 alive / 119 gold
- SOCKS5: 253 alive / 145 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17273
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
