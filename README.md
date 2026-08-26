# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 402
- HTTP: 108 alive / 59 gold
- HTTPS: 75 alive / 16 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38991
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
