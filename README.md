# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 409
- HTTP: 86 alive / 61 gold
- HTTPS: 98 alive / 22 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42689
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
