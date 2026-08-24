# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 417
- HTTP: 128 alive / 71 gold
- HTTPS: 82 alive / 20 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33811
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
