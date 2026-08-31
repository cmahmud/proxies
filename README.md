# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 436
- HTTP: 118 alive / 77 gold
- HTTPS: 73 alive / 29 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 199 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45467
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
