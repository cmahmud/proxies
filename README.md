# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 381
- HTTP: 132 alive / 61 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 171 alive / 151 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 176557
- Ever alive: 33209
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
