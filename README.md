# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 361
- HTTP: 77 alive / 48 gold
- HTTPS: 31 alive / 15 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 176 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48312
- Ever gold: 1528

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
