# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 405
- HTTP: 90 alive / 66 gold
- HTTPS: 85 alive / 21 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 177 alive / 158 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37717
- Ever gold: 1287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
