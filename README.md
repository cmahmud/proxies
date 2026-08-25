# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 413
- HTTP: 93 alive / 67 gold
- HTTPS: 80 alive / 21 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37060
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
