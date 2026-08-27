# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 422
- HTTP: 112 alive / 79 gold
- HTTPS: 113 alive / 19 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42079
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
