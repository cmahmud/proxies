# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 280
- HTTP: 293 alive / 27 gold
- HTTPS: 145 alive / 4 gold
- SOCKS4: 234 alive / 141 gold
- SOCKS5: 238 alive / 108 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12308
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
