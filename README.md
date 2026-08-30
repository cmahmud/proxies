# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 416
- HTTP: 110 alive / 67 gold
- HTTPS: 67 alive / 22 gold
- SOCKS4: 163 alive / 161 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44384
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
