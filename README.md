# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 252
- HTTP: 345 alive / 36 gold
- HTTPS: 209 alive / 8 gold
- SOCKS4: 232 alive / 141 gold
- SOCKS5: 176 alive / 67 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13716
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
