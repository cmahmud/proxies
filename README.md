# SyndProxy private pool

## Current pool

- Alive now: 634
- Gold now: 356
- HTTP: 167 alive / 71 gold
- HTTPS: 94 alive / 21 gold
- SOCKS4: 183 alive / 123 gold
- SOCKS5: 190 alive / 141 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25593
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
