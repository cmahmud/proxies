# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 372
- HTTP: 90 alive / 62 gold
- HTTPS: 59 alive / 17 gold
- SOCKS4: 151 alive / 142 gold
- SOCKS5: 170 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38876
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
