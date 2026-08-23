# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 371
- HTTP: 89 alive / 51 gold
- HTTPS: 46 alive / 11 gold
- SOCKS4: 170 alive / 154 gold
- SOCKS5: 192 alive / 155 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33030
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
