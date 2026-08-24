# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 411
- HTTP: 122 alive / 72 gold
- HTTPS: 85 alive / 18 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 193 alive / 162 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33786
- Ever gold: 1251

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
