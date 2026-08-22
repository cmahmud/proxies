# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 366
- HTTP: 257 alive / 77 gold
- HTTPS: 165 alive / 22 gold
- SOCKS4: 182 alive / 117 gold
- SOCKS5: 221 alive / 150 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32389
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
