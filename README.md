# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 389
- HTTP: 102 alive / 62 gold
- HTTPS: 72 alive / 17 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 165 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37405
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
