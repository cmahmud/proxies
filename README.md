# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 402
- HTTP: 96 alive / 61 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38979
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
