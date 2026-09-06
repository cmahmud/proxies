# SyndProxy validated proxy pool

## Current pool

- Alive now: 412
- Gold now: 333
- HTTP: 80 alive / 55 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 141 alive / 135 gold
- SOCKS5: 151 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48342
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
