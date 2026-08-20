# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 395
- HTTP: 210 alive / 73 gold
- HTTPS: 101 alive / 16 gold
- SOCKS4: 233 alive / 153 gold
- SOCKS5: 200 alive / 153 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25443
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
