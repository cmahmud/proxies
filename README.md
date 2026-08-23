# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 389
- HTTP: 116 alive / 63 gold
- HTTPS: 61 alive / 13 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33164
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
