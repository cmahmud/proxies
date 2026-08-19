# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 460
- HTTP: 402 alive / 125 gold
- HTTPS: 267 alive / 78 gold
- SOCKS4: 222 alive / 142 gold
- SOCKS5: 181 alive / 115 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17463
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
