# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 393
- HTTP: 85 alive / 66 gold
- HTTPS: 78 alive / 16 gold
- SOCKS4: 158 alive / 154 gold
- SOCKS5: 167 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43340
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
