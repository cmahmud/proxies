# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 406
- HTTP: 149 alive / 72 gold
- HTTPS: 78 alive / 17 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33774
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
