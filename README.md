# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 399
- HTTP: 333 alive / 98 gold
- HTTPS: 290 alive / 31 gold
- SOCKS4: 230 alive / 150 gold
- SOCKS5: 224 alive / 120 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30274
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
