# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 412
- HTTP: 94 alive / 62 gold
- HTTPS: 74 alive / 22 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37028
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
