# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 371
- HTTP: 89 alive / 56 gold
- HTTPS: 47 alive / 11 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 183 alive / 154 gold

## Historical pool

- Discovered: 174133
- Ever alive: 33061
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
