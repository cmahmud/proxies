# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 390
- HTTP: 100 alive / 74 gold
- HTTPS: 42 alive / 16 gold
- SOCKS4: 164 alive / 148 gold
- SOCKS5: 169 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48206
- Ever gold: 1524

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
