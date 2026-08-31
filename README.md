# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 418
- HTTP: 97 alive / 62 gold
- HTTPS: 60 alive / 25 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45488
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
