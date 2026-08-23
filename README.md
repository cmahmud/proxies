# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 197
- HTTP: 205 alive / 43 gold
- HTTPS: 67 alive / 6 gold
- SOCKS4: 102 alive / 67 gold
- SOCKS5: 134 alive / 81 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32751
- Ever gold: 1208

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
