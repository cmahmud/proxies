# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 524
- HTTP: 372 alive / 159 gold
- HTTPS: 259 alive / 91 gold
- SOCKS4: 194 alive / 135 gold
- SOCKS5: 206 alive / 139 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19894
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
