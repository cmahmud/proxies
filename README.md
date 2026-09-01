# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 461
- HTTP: 138 alive / 88 gold
- HTTPS: 120 alive / 37 gold
- SOCKS4: 168 alive / 164 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46903
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
