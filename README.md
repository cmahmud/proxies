# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 278
- HTTP: 305 alive / 37 gold
- HTTPS: 189 alive / 8 gold
- SOCKS4: 219 alive / 138 gold
- SOCKS5: 166 alive / 95 gold

## Historical pool

- Discovered: 102915
- Ever alive: 13931
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
