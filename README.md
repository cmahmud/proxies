# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 413
- HTTP: 105 alive / 67 gold
- HTTPS: 98 alive / 16 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38031
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
