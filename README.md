# SyndProxy validated proxy pool

## Current pool

- Alive now: 424
- Gold now: 329
- HTTP: 86 alive / 56 gold
- HTTPS: 47 alive / 17 gold
- SOCKS4: 146 alive / 132 gold
- SOCKS5: 145 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48344
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
