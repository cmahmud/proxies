# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 403
- HTTP: 347 alive / 90 gold
- HTTPS: 241 alive / 27 gold
- SOCKS4: 179 alive / 116 gold
- SOCKS5: 250 alive / 170 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32452
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
