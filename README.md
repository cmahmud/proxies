# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 386
- HTTP: 106 alive / 55 gold
- HTTPS: 54 alive / 12 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33440
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
