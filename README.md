# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 397
- HTTP: 378 alive / 103 gold
- HTTPS: 267 alive / 24 gold
- SOCKS4: 188 alive / 125 gold
- SOCKS5: 306 alive / 145 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22616
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
