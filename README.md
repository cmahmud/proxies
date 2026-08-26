# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 383
- HTTP: 116 alive / 69 gold
- HTTPS: 52 alive / 17 gold
- SOCKS4: 156 alive / 141 gold
- SOCKS5: 174 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38922
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
