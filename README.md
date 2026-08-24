# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 406
- HTTP: 148 alive / 73 gold
- HTTPS: 85 alive / 17 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 190 alive / 159 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33775
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
