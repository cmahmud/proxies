# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 304
- HTTP: 165 alive / 36 gold
- HTTPS: 64 alive / 12 gold
- SOCKS4: 179 alive / 152 gold
- SOCKS5: 195 alive / 104 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32837
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
