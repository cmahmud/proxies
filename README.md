# SyndProxy private pool

## Current pool

- Alive now: 693
- Gold now: 381
- HTTP: 167 alive / 74 gold
- HTTPS: 118 alive / 19 gold
- SOCKS4: 200 alive / 139 gold
- SOCKS5: 208 alive / 149 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25510
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
