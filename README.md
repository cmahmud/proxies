# SyndProxy private pool

## Current pool

- Alive now: 1653
- Gold now: 592
- HTTP: 664 alive / 186 gold
- HTTPS: 518 alive / 94 gold
- SOCKS4: 225 alive / 144 gold
- SOCKS5: 246 alive / 168 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24003
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
