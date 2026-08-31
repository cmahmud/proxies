# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 409
- HTTP: 95 alive / 57 gold
- HTTPS: 71 alive / 23 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45505
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
