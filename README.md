# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 442
- HTTP: 135 alive / 88 gold
- HTTPS: 102 alive / 23 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34267
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
