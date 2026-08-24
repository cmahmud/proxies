# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 387
- HTTP: 130 alive / 57 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 191 alive / 162 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33654
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
