# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 423
- HTTP: 117 alive / 77 gold
- HTTPS: 133 alive / 23 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 198 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42391
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
