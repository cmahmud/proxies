# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 407
- HTTP: 94 alive / 60 gold
- HTTPS: 89 alive / 21 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42719
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
