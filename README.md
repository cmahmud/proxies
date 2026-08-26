# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 399
- HTTP: 90 alive / 56 gold
- HTTPS: 32 alive / 16 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38976
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
