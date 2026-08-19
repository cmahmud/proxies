# SyndProxy private pool

## Current pool

- Alive now: 1132
- Gold now: 589
- HTTP: 416 alive / 185 gold
- HTTPS: 309 alive / 129 gold
- SOCKS4: 206 alive / 132 gold
- SOCKS5: 201 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19827
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
