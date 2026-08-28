# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 413
- HTTP: 102 alive / 69 gold
- HTTPS: 100 alive / 21 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42614
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
