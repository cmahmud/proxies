# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 404
- HTTP: 277 alive / 93 gold
- HTTPS: 158 alive / 20 gold
- SOCKS4: 212 alive / 152 gold
- SOCKS5: 236 alive / 139 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29234
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
