# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 397
- HTTP: 152 alive / 67 gold
- HTTPS: 61 alive / 15 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33285
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
