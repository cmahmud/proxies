# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 411
- HTTP: 124 alive / 73 gold
- HTTPS: 81 alive / 18 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 195 alive / 161 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33781
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
