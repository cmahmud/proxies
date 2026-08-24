# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 386
- HTTP: 99 alive / 63 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33439
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
