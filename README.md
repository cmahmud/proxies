# SyndProxy private pool

## Current pool

- Alive now: 1255
- Gold now: 562
- HTTP: 511 alive / 193 gold
- HTTPS: 329 alive / 98 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 198 alive / 131 gold

## Historical pool

- Discovered: 136254
- Ever alive: 22784
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
