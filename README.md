# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 380
- HTTP: 103 alive / 63 gold
- HTTPS: 68 alive / 21 gold
- SOCKS4: 149 alive / 141 gold
- SOCKS5: 173 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38763
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
