# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 293
- HTTP: 109 alive / 77 gold
- HTTPS: 35 alive / 19 gold
- SOCKS4: 77 alive / 65 gold
- SOCKS5: 158 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47859
- Ever gold: 1499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
