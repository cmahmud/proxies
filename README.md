# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 425
- HTTP: 95 alive / 72 gold
- HTTPS: 81 alive / 22 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37977
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
