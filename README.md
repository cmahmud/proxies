# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 462
- HTTP: 384 alive / 126 gold
- HTTPS: 282 alive / 79 gold
- SOCKS4: 211 alive / 143 gold
- SOCKS5: 195 alive / 114 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17457
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
