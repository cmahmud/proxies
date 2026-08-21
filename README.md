# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 399
- HTTP: 244 alive / 90 gold
- HTTPS: 147 alive / 18 gold
- SOCKS4: 215 alive / 152 gold
- SOCKS5: 233 alive / 139 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29240
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
