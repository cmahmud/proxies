# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 414
- HTTP: 123 alive / 74 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 181477
- Ever alive: 33767
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
