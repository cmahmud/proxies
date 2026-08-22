# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 371
- HTTP: 348 alive / 81 gold
- HTTPS: 257 alive / 25 gold
- SOCKS4: 202 alive / 137 gold
- SOCKS5: 236 alive / 128 gold

## Historical pool

- Discovered: 165837
- Ever alive: 32366
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
