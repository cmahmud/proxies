# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 331
- HTTP: 103 alive / 37 gold
- HTTPS: 84 alive / 5 gold
- SOCKS4: 164 alive / 150 gold
- SOCKS5: 185 alive / 139 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32903
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
