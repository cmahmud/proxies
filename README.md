# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 426
- HTTP: 120 alive / 80 gold
- HTTPS: 170 alive / 19 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42303
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
