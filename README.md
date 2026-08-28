# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 407
- HTTP: 99 alive / 65 gold
- HTTPS: 101 alive / 16 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42665
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
