# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 392
- HTTP: 132 alive / 58 gold
- HTTPS: 58 alive / 14 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33641
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
