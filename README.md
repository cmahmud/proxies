# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 340
- HTTP: 145 alive / 37 gold
- HTTPS: 65 alive / 11 gold
- SOCKS4: 172 alive / 152 gold
- SOCKS5: 193 alive / 140 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32837
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
