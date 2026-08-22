# SyndProxy private pool

## Current pool

- Alive now: 842
- Gold now: 372
- HTTP: 274 alive / 81 gold
- HTTPS: 170 alive / 23 gold
- SOCKS4: 178 alive / 118 gold
- SOCKS5: 220 alive / 150 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32389
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
