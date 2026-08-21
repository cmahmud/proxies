# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 416
- HTTP: 352 alive / 105 gold
- HTTPS: 268 alive / 31 gold
- SOCKS4: 225 alive / 139 gold
- SOCKS5: 236 alive / 141 gold

## Historical pool

- Discovered: 160253
- Ever alive: 30691
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
