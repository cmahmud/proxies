# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 389
- HTTP: 94 alive / 58 gold
- HTTPS: 60 alive / 14 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33503
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
