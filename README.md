# SyndProxy private pool

## Current pool

- Alive now: 1270
- Gold now: 573
- HTTP: 517 alive / 196 gold
- HTTPS: 309 alive / 94 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 221 alive / 135 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22845
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
