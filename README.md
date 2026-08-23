# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 371
- HTTP: 74 alive / 52 gold
- HTTPS: 35 alive / 11 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 177 alive / 154 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33047
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
