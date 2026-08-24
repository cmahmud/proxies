# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 387
- HTTP: 108 alive / 72 gold
- HTTPS: 68 alive / 14 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 178 alive / 151 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33236
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
