# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 522
- HTTP: 348 alive / 154 gold
- HTTPS: 249 alive / 92 gold
- SOCKS4: 195 alive / 133 gold
- SOCKS5: 212 alive / 143 gold

## Historical pool

- Discovered: 127362
- Ever alive: 19895
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
