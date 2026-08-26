# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 413
- HTTP: 99 alive / 66 gold
- HTTPS: 78 alive / 21 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37775
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
