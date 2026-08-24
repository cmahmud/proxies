# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 377
- HTTP: 115 alive / 56 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 177 alive / 156 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33439
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
