# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 413
- HTTP: 110 alive / 65 gold
- HTTPS: 82 alive / 21 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37074
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
