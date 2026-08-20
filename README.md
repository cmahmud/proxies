# SyndProxy private pool

## Current pool

- Alive now: 830
- Gold now: 382
- HTTP: 220 alive / 80 gold
- HTTPS: 158 alive / 21 gold
- SOCKS4: 206 alive / 141 gold
- SOCKS5: 246 alive / 140 gold

## Historical pool

- Discovered: 144768
- Ever alive: 25274
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
