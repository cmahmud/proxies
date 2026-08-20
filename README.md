# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 368
- HTTP: 192 alive / 67 gold
- HTTPS: 136 alive / 17 gold
- SOCKS4: 201 alive / 134 gold
- SOCKS5: 208 alive / 150 gold

## Historical pool

- Discovered: 145550
- Ever alive: 25408
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
