# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 377
- HTTP: 112 alive / 57 gold
- HTTPS: 37 alive / 9 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 176 alive / 156 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33439
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
