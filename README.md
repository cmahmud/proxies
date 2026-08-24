# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 407
- HTTP: 145 alive / 72 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33773
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
