# SyndProxy validated proxy pool

## Current pool

- Alive now: 421
- Gold now: 315
- HTTP: 142 alive / 78 gold
- HTTPS: 30 alive / 21 gold
- SOCKS4: 80 alive / 70 gold
- SOCKS5: 169 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47824
- Ever gold: 1495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
