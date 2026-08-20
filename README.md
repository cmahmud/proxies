# SyndProxy private pool

## Current pool

- Alive now: 1134
- Gold now: 594
- HTTP: 374 alive / 188 gold
- HTTPS: 316 alive / 101 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 232 alive / 159 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23458
- Ever gold: 921

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
