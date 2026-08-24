# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 376
- HTTP: 123 alive / 54 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 183 alive / 156 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33442
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
