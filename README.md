# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 399
- HTTP: 91 alive / 62 gold
- HTTPS: 82 alive / 22 gold
- SOCKS4: 182 alive / 159 gold
- SOCKS5: 178 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37581
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
