# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 438
- HTTP: 109 alive / 82 gold
- HTTPS: 62 alive / 24 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44563
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
