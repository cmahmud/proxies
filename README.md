# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 392
- HTTP: 145 alive / 56 gold
- HTTPS: 62 alive / 15 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33641
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
