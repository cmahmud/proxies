# SyndProxy validated proxy pool

## Current pool

- Alive now: 428
- Gold now: 344
- HTTP: 91 alive / 65 gold
- HTTPS: 38 alive / 14 gold
- SOCKS4: 151 alive / 138 gold
- SOCKS5: 148 alive / 127 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48377
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
