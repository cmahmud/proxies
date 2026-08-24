# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 410
- HTTP: 131 alive / 72 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33796
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
