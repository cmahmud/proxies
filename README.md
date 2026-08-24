# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 376
- HTTP: 100 alive / 52 gold
- HTTPS: 63 alive / 8 gold
- SOCKS4: 176 alive / 155 gold
- SOCKS5: 195 alive / 161 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33449
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
