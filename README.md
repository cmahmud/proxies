# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 409
- HTTP: 106 alive / 67 gold
- HTTPS: 53 alive / 17 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38952
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
