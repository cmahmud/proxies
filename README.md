# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 410
- HTTP: 140 alive / 74 gold
- HTTPS: 89 alive / 18 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 194 alive / 160 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33779
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
