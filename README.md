# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 495
- HTTP: 420 alive / 124 gold
- HTTPS: 311 alive / 71 gold
- SOCKS4: 225 alive / 150 gold
- SOCKS5: 260 alive / 150 gold

## Historical pool

- Discovered: 116452
- Ever alive: 17127
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
