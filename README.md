# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 390
- HTTP: 113 alive / 59 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33440
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
