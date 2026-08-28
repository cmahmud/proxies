# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 407
- HTTP: 104 alive / 63 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42659
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
