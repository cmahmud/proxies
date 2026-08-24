# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 410
- HTTP: 128 alive / 73 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33772
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
