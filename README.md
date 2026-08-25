# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 393
- HTTP: 100 alive / 64 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 168 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37499
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
