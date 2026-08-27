# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 391
- HTTP: 77 alive / 47 gold
- HTTPS: 56 alive / 14 gold
- SOCKS4: 176 alive / 165 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41613
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
