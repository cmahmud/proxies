# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 369
- HTTP: 81 alive / 53 gold
- HTTPS: 32 alive / 11 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48278
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
