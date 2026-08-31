# SyndProxy validated proxy pool

## Current pool

- Alive now: 720
- Gold now: 473
- HTTP: 196 alive / 98 gold
- HTTPS: 119 alive / 38 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 231 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45293
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
