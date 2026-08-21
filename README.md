# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 390
- HTTP: 262 alive / 89 gold
- HTTPS: 181 alive / 24 gold
- SOCKS4: 223 alive / 140 gold
- SOCKS5: 231 alive / 137 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29373
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
