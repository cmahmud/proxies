# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 408
- HTTP: 98 alive / 62 gold
- HTTPS: 79 alive / 20 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 190 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42655
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
