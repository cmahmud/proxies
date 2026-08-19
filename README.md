# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 400
- HTTP: 310 alive / 76 gold
- HTTPS: 246 alive / 13 gold
- SOCKS4: 254 alive / 152 gold
- SOCKS5: 249 alive / 159 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20546
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
