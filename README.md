# SyndProxy private pool

## Current pool

- Alive now: 890
- Gold now: 277
- HTTP: 300 alive / 37 gold
- HTTPS: 152 alive / 9 gold
- SOCKS4: 250 alive / 139 gold
- SOCKS5: 188 alive / 92 gold

## Historical pool

- Discovered: 102895
- Ever alive: 13877
- Ever gold: 431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
