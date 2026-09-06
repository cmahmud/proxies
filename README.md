# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 378
- HTTP: 137 alive / 82 gold
- HTTPS: 57 alive / 23 gold
- SOCKS4: 152 alive / 124 gold
- SOCKS5: 181 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48006
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
