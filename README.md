# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 396
- HTTP: 114 alive / 73 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 185 alive / 156 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33276
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
