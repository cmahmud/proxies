# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 413
- HTTP: 101 alive / 68 gold
- HTTPS: 75 alive / 20 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38648
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
