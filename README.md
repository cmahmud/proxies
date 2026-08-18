# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 227
- HTTP: 314 alive / 31 gold
- HTTPS: 157 alive / 8 gold
- SOCKS4: 230 alive / 124 gold
- SOCKS5: 155 alive / 64 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13537
- Ever gold: 424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
