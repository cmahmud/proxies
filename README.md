# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 340
- HTTP: 120 alive / 39 gold
- HTTPS: 63 alive / 11 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 188 alive / 139 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32823
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
