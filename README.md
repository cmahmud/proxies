# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 412
- HTTP: 123 alive / 73 gold
- HTTPS: 86 alive / 18 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 193 alive / 162 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33783
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
