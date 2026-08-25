# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 402
- HTTP: 109 alive / 71 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 166 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37443
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
