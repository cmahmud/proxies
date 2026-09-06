# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 342
- HTTP: 77 alive / 53 gold
- HTTPS: 29 alive / 6 gold
- SOCKS4: 165 alive / 140 gold
- SOCKS5: 177 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48289
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
