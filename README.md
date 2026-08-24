# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 389
- HTTP: 146 alive / 57 gold
- HTTPS: 51 alive / 13 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 197 alive / 162 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33652
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
