# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 370
- HTTP: 96 alive / 57 gold
- HTTPS: 54 alive / 18 gold
- SOCKS4: 157 alive / 143 gold
- SOCKS5: 168 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38857
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
