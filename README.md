# SyndProxy validated proxy pool

## Current pool

- Alive now: 424
- Gold now: 312
- HTTP: 82 alive / 53 gold
- HTTPS: 45 alive / 7 gold
- SOCKS4: 149 alive / 133 gold
- SOCKS5: 148 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48368
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
