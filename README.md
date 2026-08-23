# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 348
- HTTP: 228 alive / 40 gold
- HTTPS: 45 alive / 9 gold
- SOCKS4: 184 alive / 153 gold
- SOCKS5: 192 alive / 146 gold

## Historical pool

- Discovered: 171088
- Ever alive: 32864
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
