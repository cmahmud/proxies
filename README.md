# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 399
- HTTP: 106 alive / 67 gold
- HTTPS: 80 alive / 17 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 169 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37331
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
