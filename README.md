# SyndProxy validated proxy pool

## Current pool

- Alive now: 375
- Gold now: 296
- HTTP: 105 alive / 79 gold
- HTTPS: 34 alive / 19 gold
- SOCKS4: 77 alive / 65 gold
- SOCKS5: 159 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47859
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
