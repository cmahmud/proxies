# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 393
- HTTP: 102 alive / 60 gold
- HTTPS: 61 alive / 13 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
