# SyndProxy private pool

## Current pool

- Alive now: 895
- Gold now: 403
- HTTP: 281 alive / 93 gold
- HTTPS: 160 alive / 19 gold
- SOCKS4: 217 alive / 152 gold
- SOCKS5: 237 alive / 139 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29240
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
