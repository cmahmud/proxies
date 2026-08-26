# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 383
- HTTP: 103 alive / 60 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 154 alive / 149 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38930
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
