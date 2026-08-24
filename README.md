# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 417
- HTTP: 129 alive / 69 gold
- HTTPS: 82 alive / 20 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33814
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
