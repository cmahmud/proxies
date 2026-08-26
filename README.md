# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 378
- HTTP: 103 alive / 67 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 152 alive / 143 gold
- SOCKS5: 176 alive / 150 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38788
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
