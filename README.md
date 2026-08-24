# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 410
- HTTP: 120 alive / 73 gold
- HTTPS: 68 alive / 18 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33770
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
