# SyndProxy private pool

## Current pool

- Alive now: 1186
- Gold now: 562
- HTTP: 432 alive / 184 gold
- HTTPS: 304 alive / 101 gold
- SOCKS4: 212 alive / 124 gold
- SOCKS5: 238 alive / 153 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19263
- Ever gold: 770

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
