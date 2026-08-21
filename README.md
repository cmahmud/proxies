# SyndProxy private pool

## Current pool

- Alive now: 1126
- Gold now: 453
- HTTP: 412 alive / 103 gold
- HTTPS: 240 alive / 30 gold
- SOCKS4: 216 alive / 152 gold
- SOCKS5: 258 alive / 168 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28730
- Ever gold: 1113

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
