# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 388
- HTTP: 129 alive / 54 gold
- HTTPS: 48 alive / 14 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33634
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
