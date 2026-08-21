# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 402
- HTTP: 285 alive / 94 gold
- HTTPS: 225 alive / 19 gold
- SOCKS4: 221 alive / 150 gold
- SOCKS5: 245 alive / 139 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29261
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
