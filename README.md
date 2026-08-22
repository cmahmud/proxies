# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 437
- HTTP: 338 alive / 88 gold
- HTTPS: 215 alive / 28 gold
- SOCKS4: 236 alive / 159 gold
- SOCKS5: 276 alive / 162 gold

## Historical pool

- Discovered: 164942
- Ever alive: 32197
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
