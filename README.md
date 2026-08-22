# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 332
- HTTP: 315 alive / 82 gold
- HTTPS: 211 alive / 26 gold
- SOCKS4: 207 alive / 138 gold
- SOCKS5: 191 alive / 86 gold

## Historical pool

- Discovered: 167104
- Ever alive: 32512
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
