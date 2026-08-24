# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 415
- HTTP: 115 alive / 75 gold
- HTTPS: 68 alive / 19 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33768
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
