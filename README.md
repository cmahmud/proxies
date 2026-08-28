# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 413
- HTTP: 93 alive / 66 gold
- HTTPS: 87 alive / 21 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42655
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
