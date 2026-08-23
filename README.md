# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 341
- HTTP: 114 alive / 38 gold
- HTTPS: 70 alive / 11 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 184 alive / 141 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32823
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
