# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 555
- HTTP: 419 alive / 190 gold
- HTTPS: 284 alive / 104 gold
- SOCKS4: 207 alive / 120 gold
- SOCKS5: 205 alive / 141 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19300
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
