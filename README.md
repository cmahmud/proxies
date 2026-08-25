# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 413
- HTTP: 93 alive / 67 gold
- HTTPS: 78 alive / 21 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 172 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37058
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
