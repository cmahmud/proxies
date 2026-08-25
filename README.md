# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 405
- HTTP: 101 alive / 68 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 167 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37311
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
