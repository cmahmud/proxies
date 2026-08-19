# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 548
- HTTP: 392 alive / 180 gold
- HTTPS: 267 alive / 113 gold
- SOCKS4: 205 alive / 116 gold
- SOCKS5: 192 alive / 139 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19304
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
