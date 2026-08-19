# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 505
- HTTP: 339 alive / 158 gold
- HTTPS: 256 alive / 88 gold
- SOCKS4: 207 alive / 141 gold
- SOCKS5: 194 alive / 118 gold

## Historical pool

- Discovered: 119845
- Ever alive: 18376
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
