# SyndProxy private pool

## Current pool

- Alive now: 1318
- Gold now: 573
- HTTP: 527 alive / 196 gold
- HTTPS: 344 alive / 94 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 225 alive / 134 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22845
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
