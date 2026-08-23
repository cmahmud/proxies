# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 373
- HTTP: 109 alive / 50 gold
- HTTPS: 44 alive / 12 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 188 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33034
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
