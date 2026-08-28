# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 410
- HTTP: 96 alive / 67 gold
- HTTPS: 123 alive / 18 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42630
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
