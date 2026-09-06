# SyndProxy validated proxy pool

## Current pool

- Alive now: 417
- Gold now: 340
- HTTP: 82 alive / 63 gold
- HTTPS: 32 alive / 14 gold
- SOCKS4: 149 alive / 138 gold
- SOCKS5: 154 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48377
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
