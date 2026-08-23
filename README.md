# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 336
- HTTP: 101 alive / 37 gold
- HTTPS: 82 alive / 5 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 185 alive / 143 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32903
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
