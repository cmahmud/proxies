# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 437
- HTTP: 318 alive / 90 gold
- HTTPS: 208 alive / 27 gold
- SOCKS4: 237 alive / 148 gold
- SOCKS5: 282 alive / 172 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31024
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
