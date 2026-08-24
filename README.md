# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 415
- HTTP: 130 alive / 68 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33816
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
