# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 413
- HTTP: 100 alive / 68 gold
- HTTPS: 93 alive / 19 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42672
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
