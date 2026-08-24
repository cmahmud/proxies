# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 414
- HTTP: 106 alive / 74 gold
- HTTPS: 62 alive / 18 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33721
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
