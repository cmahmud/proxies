# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 413
- HTTP: 97 alive / 67 gold
- HTTPS: 100 alive / 19 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42625
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
