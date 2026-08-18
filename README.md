# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 249
- HTTP: 305 alive / 33 gold
- HTTPS: 222 alive / 7 gold
- SOCKS4: 248 alive / 143 gold
- SOCKS5: 161 alive / 66 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13748
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
