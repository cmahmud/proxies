# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 413
- HTTP: 94 alive / 64 gold
- HTTPS: 71 alive / 22 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37041
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
