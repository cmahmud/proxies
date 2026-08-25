# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 394
- HTTP: 99 alive / 62 gold
- HTTPS: 70 alive / 20 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 159 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37517
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
