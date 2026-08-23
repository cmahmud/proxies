# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 347
- HTTP: 115 alive / 33 gold
- HTTPS: 37 alive / 8 gold
- SOCKS4: 179 alive / 151 gold
- SOCKS5: 198 alive / 155 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32953
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
