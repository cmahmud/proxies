# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 397
- HTTP: 376 alive / 104 gold
- HTTPS: 260 alive / 23 gold
- SOCKS4: 206 alive / 125 gold
- SOCKS5: 306 alive / 145 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22630
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
