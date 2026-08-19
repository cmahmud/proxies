# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 374
- HTTP: 315 alive / 76 gold
- HTTPS: 210 alive / 12 gold
- SOCKS4: 230 alive / 134 gold
- SOCKS5: 231 alive / 152 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20389
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
