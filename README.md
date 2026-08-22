# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 362
- HTTP: 295 alive / 76 gold
- HTTPS: 187 alive / 25 gold
- SOCKS4: 203 alive / 132 gold
- SOCKS5: 225 alive / 129 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32354
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
