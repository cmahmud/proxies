# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 512
- HTTP: 356 alive / 152 gold
- HTTPS: 262 alive / 88 gold
- SOCKS4: 188 alive / 133 gold
- SOCKS5: 203 alive / 139 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
