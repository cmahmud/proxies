# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 416
- HTTP: 141 alive / 68 gold
- HTTPS: 85 alive / 20 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33816
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
