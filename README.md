# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 410
- HTTP: 97 alive / 66 gold
- HTTPS: 96 alive / 17 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42666
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
