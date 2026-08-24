# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 390
- HTTP: 97 alive / 59 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 179 alive / 160 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33504
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
