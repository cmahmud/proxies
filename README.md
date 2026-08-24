# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 398
- HTTP: 134 alive / 61 gold
- HTTPS: 72 alive / 15 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
