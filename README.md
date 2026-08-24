# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 390
- HTTP: 136 alive / 57 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 199 alive / 162 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33652
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
