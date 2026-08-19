# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 538
- HTTP: 363 alive / 170 gold
- HTTPS: 240 alive / 90 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 219 alive / 142 gold

## Historical pool

- Discovered: 122380
- Ever alive: 18651
- Ever gold: 727

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
