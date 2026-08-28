# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 424
- HTTP: 117 alive / 76 gold
- HTTPS: 141 alive / 21 gold
- SOCKS4: 182 alive / 159 gold
- SOCKS5: 196 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42363
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
