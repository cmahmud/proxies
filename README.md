# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 421
- HTTP: 107 alive / 72 gold
- HTTPS: 85 alive / 21 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 176 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37850
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
