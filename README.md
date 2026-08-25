# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 402
- HTTP: 106 alive / 70 gold
- HTTPS: 76 alive / 19 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37449
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
