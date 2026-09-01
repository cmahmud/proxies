# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 426
- HTTP: 81 alive / 68 gold
- HTTPS: 78 alive / 27 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47151
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
