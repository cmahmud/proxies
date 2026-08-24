# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 392
- HTTP: 113 alive / 58 gold
- HTTPS: 63 alive / 15 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 196 alive / 162 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33651
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
