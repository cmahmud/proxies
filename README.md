# SyndProxy private pool

## Current pool

- Alive now: 1386
- Gold now: 604
- HTTP: 545 alive / 196 gold
- HTTPS: 369 alive / 100 gold
- SOCKS4: 213 alive / 140 gold
- SOCKS5: 259 alive / 168 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23111
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
