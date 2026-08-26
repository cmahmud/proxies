# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 413
- HTTP: 101 alive / 66 gold
- HTTPS: 85 alive / 22 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37770
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
