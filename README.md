# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 396
- HTTP: 147 alive / 71 gold
- HTTPS: 71 alive / 15 gold
- SOCKS4: 178 alive / 156 gold
- SOCKS5: 191 alive / 154 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33268
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
