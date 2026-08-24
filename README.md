# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 416
- HTTP: 134 alive / 68 gold
- HTTPS: 81 alive / 20 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33821
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
