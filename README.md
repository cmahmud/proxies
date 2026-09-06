# SyndProxy validated proxy pool

## Current pool

- Alive now: 430
- Gold now: 343
- HTTP: 93 alive / 64 gold
- HTTPS: 42 alive / 17 gold
- SOCKS4: 149 alive / 137 gold
- SOCKS5: 146 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48362
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
