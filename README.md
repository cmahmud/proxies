# SyndProxy private pool

## Current pool

- Alive now: 1536
- Gold now: 579
- HTTP: 655 alive / 189 gold
- HTTPS: 377 alive / 91 gold
- SOCKS4: 237 alive / 140 gold
- SOCKS5: 267 alive / 159 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23153
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
