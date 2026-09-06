# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 360
- HTTP: 77 alive / 48 gold
- HTTPS: 40 alive / 9 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 182 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48289
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
