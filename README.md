# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 343
- HTTP: 112 alive / 42 gold
- HTTPS: 103 alive / 9 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 180 alive / 140 gold

## Historical pool

- Discovered: 171031
- Ever alive: 32798
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
