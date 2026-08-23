# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 305
- HTTP: 162 alive / 37 gold
- HTTPS: 63 alive / 12 gold
- SOCKS4: 178 alive / 152 gold
- SOCKS5: 192 alive / 104 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32837
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
