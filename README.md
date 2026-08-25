# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 414
- HTTP: 105 alive / 71 gold
- HTTPS: 89 alive / 22 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 170 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37160
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
