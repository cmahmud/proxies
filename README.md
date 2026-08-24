# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 412
- HTTP: 114 alive / 74 gold
- HTTPS: 70 alive / 18 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33768
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
