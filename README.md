# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 190
- HTTP: 176 alive / 39 gold
- HTTPS: 78 alive / 6 gold
- SOCKS4: 91 alive / 65 gold
- SOCKS5: 135 alive / 80 gold

## Historical pool

- Discovered: 170282
- Ever alive: 32751
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
