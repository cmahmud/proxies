# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 412
- HTTP: 96 alive / 67 gold
- HTTPS: 95 alive / 18 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42667
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
