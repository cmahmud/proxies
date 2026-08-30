# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 442
- HTTP: 126 alive / 89 gold
- HTTPS: 84 alive / 29 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44287
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
