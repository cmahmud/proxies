# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 407
- HTTP: 101 alive / 62 gold
- HTTPS: 80 alive / 19 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42656
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
