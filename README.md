# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 411
- HTTP: 208 alive / 83 gold
- HTTPS: 138 alive / 25 gold
- SOCKS4: 210 alive / 145 gold
- SOCKS5: 261 alive / 158 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29349
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
