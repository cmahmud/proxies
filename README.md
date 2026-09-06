# SyndProxy validated proxy pool

## Current pool

- Alive now: 412
- Gold now: 326
- HTTP: 77 alive / 54 gold
- HTTPS: 42 alive / 18 gold
- SOCKS4: 144 alive / 131 gold
- SOCKS5: 149 alive / 123 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48339
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
