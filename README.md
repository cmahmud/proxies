# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 392
- HTTP: 97 alive / 62 gold
- HTTPS: 36 alive / 12 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 176 alive / 162 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33439
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
