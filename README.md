# SyndProxy private pool

## Current pool

- Alive now: 1237
- Gold now: 403
- HTTP: 412 alive / 93 gold
- HTTPS: 314 alive / 20 gold
- SOCKS4: 225 alive / 139 gold
- SOCKS5: 286 alive / 151 gold

## Historical pool

- Discovered: 135216
- Ever alive: 22200
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
