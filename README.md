# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 274
- HTTP: 293 alive / 37 gold
- HTTPS: 201 alive / 8 gold
- SOCKS4: 230 alive / 139 gold
- SOCKS5: 159 alive / 90 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13778
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
