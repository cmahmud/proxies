# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 381
- HTTP: 120 alive / 62 gold
- HTTPS: 43 alive / 16 gold
- SOCKS4: 172 alive / 151 gold
- SOCKS5: 176 alive / 152 gold

## Historical pool

- Discovered: 176557
- Ever alive: 33209
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
