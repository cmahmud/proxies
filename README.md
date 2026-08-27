# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 418
- HTTP: 112 alive / 72 gold
- HTTPS: 165 alive / 18 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41197
- Ever gold: 1318

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
