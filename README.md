# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 410
- HTTP: 132 alive / 72 gold
- HTTPS: 76 alive / 18 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33790
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
