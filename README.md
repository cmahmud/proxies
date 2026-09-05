# SyndProxy validated proxy pool

## Current pool

- Alive now: 392
- Gold now: 314
- HTTP: 105 alive / 77 gold
- HTTPS: 34 alive / 16 gold
- SOCKS4: 82 alive / 73 gold
- SOCKS5: 171 alive / 148 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47833
- Ever gold: 1497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
