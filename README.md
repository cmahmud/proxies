# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 478
- HTTP: 335 alive / 120 gold
- HTTPS: 221 alive / 72 gold
- SOCKS4: 234 alive / 141 gold
- SOCKS5: 255 alive / 145 gold

## Historical pool

- Discovered: 113577
- Ever alive: 16887
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
