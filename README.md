# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 422
- HTTP: 117 alive / 74 gold
- HTTPS: 69 alive / 24 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44340
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
