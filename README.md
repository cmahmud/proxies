# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 411
- HTTP: 134 alive / 72 gold
- HTTPS: 89 alive / 18 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 187 alive / 162 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33798
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
