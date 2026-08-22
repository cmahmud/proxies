# SyndProxy private pool

## Current pool

- Alive now: 828
- Gold now: 373
- HTTP: 272 alive / 81 gold
- HTTPS: 140 alive / 21 gold
- SOCKS4: 187 alive / 119 gold
- SOCKS5: 229 alive / 152 gold

## Historical pool

- Discovered: 166324
- Ever alive: 32393
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
