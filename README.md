# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 399
- HTTP: 95 alive / 56 gold
- HTTPS: 102 alive / 16 gold
- SOCKS4: 182 alive / 167 gold
- SOCKS5: 191 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41522
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
