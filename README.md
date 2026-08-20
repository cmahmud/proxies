# SyndProxy private pool

## Current pool

- Alive now: 805
- Gold now: 386
- HTTP: 234 alive / 79 gold
- HTTPS: 124 alive / 16 gold
- SOCKS4: 231 alive / 153 gold
- SOCKS5: 216 alive / 138 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25467
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
