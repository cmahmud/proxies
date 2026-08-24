# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 432
- HTTP: 122 alive / 77 gold
- HTTPS: 86 alive / 25 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34662
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
