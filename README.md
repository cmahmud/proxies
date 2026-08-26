# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 396
- HTTP: 102 alive / 64 gold
- HTTPS: 47 alive / 16 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38939
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
