# SyndProxy validated proxy pool

## Current pool

- Alive now: 328
- Gold now: 203
- HTTP: 35 alive / 14 gold
- HTTPS: 2 alive / 0 gold
- SOCKS4: 146 alive / 103 gold
- SOCKS5: 145 alive / 86 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43627
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
