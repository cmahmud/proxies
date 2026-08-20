# SyndProxy private pool

## Current pool

- Alive now: 752
- Gold now: 379
- HTTP: 209 alive / 71 gold
- HTTPS: 102 alive / 21 gold
- SOCKS4: 234 alive / 144 gold
- SOCKS5: 207 alive / 143 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25426
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
