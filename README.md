# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 395
- HTTP: 257 alive / 87 gold
- HTTPS: 160 alive / 22 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 246 alive / 139 gold

## Historical pool

- Discovered: 155693
- Ever alive: 29225
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
