# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 382
- HTTP: 192 alive / 73 gold
- HTTPS: 103 alive / 16 gold
- SOCKS4: 214 alive / 138 gold
- SOCKS5: 216 alive / 155 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25802
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
