# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 429
- HTTP: 125 alive / 79 gold
- HTTPS: 102 alive / 23 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34054
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
