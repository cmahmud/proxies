# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 506
- HTTP: 444 alive / 175 gold
- HTTPS: 305 alive / 114 gold
- SOCKS4: 213 alive / 105 gold
- SOCKS5: 183 alive / 112 gold

## Historical pool

- Discovered: 124843
- Ever alive: 19330
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
