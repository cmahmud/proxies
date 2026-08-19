# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 523
- HTTP: 375 alive / 157 gold
- HTTPS: 260 alive / 92 gold
- SOCKS4: 192 alive / 135 gold
- SOCKS5: 202 alive / 139 gold

## Historical pool

- Discovered: 127357
- Ever alive: 19894
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
