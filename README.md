# SyndProxy validated proxy pool

## Current pool

- Alive now: 407
- Gold now: 311
- HTTP: 82 alive / 56 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 142 alive / 129 gold
- SOCKS5: 146 alive / 114 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48370
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
