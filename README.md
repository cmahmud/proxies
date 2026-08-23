# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 368
- HTTP: 82 alive / 47 gold
- HTTPS: 38 alive / 11 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 189 alive / 156 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33027
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
