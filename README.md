# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 256
- HTTP: 412 alive / 30 gold
- HTTPS: 176 alive / 4 gold
- SOCKS4: 211 alive / 117 gold
- SOCKS5: 220 alive / 105 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11775
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
