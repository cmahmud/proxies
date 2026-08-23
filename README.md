# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 358
- HTTP: 86 alive / 36 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 176 alive / 157 gold

## Historical pool

- Discovered: 171794
- Ever alive: 32947
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
