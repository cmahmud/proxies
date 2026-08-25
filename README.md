# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 393
- HTTP: 103 alive / 65 gold
- HTTPS: 84 alive / 16 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 162 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37465
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
