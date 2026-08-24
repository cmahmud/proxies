# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 375
- HTTP: 141 alive / 68 gold
- HTTPS: 44 alive / 13 gold
- SOCKS4: 164 alive / 148 gold
- SOCKS5: 177 alive / 146 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33228
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
