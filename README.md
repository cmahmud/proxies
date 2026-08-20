# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 375
- HTTP: 209 alive / 69 gold
- HTTPS: 113 alive / 22 gold
- SOCKS4: 223 alive / 143 gold
- SOCKS5: 206 alive / 141 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25424
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
