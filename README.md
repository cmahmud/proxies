# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 402
- HTTP: 164 alive / 71 gold
- HTTPS: 78 alive / 13 gold
- SOCKS4: 189 alive / 156 gold
- SOCKS5: 203 alive / 162 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33304
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
