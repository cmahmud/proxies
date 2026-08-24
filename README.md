# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 416
- HTTP: 115 alive / 74 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33736
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
