# SyndProxy private pool

## Current pool

- Alive now: 743
- Gold now: 387
- HTTP: 186 alive / 89 gold
- HTTPS: 139 alive / 28 gold
- SOCKS4: 206 alive / 125 gold
- SOCKS5: 212 alive / 145 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27296
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
