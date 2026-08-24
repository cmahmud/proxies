# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 417
- HTTP: 145 alive / 74 gold
- HTTPS: 74 alive / 18 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 199 alive / 167 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33739
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
