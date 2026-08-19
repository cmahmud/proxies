# SyndProxy private pool

## Current pool

- Alive now: 1122
- Gold now: 542
- HTTP: 433 alive / 165 gold
- HTTPS: 263 alive / 93 gold
- SOCKS4: 215 alive / 144 gold
- SOCKS5: 211 alive / 140 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18858
- Ever gold: 729

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
