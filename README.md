# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 365
- HTTP: 385 alive / 98 gold
- HTTPS: 270 alive / 22 gold
- SOCKS4: 175 alive / 113 gold
- SOCKS5: 230 alive / 132 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28811
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
