# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 408
- HTTP: 414 alive / 103 gold
- HTTPS: 249 alive / 24 gold
- SOCKS4: 221 alive / 132 gold
- SOCKS5: 263 alive / 149 gold

## Historical pool

- Discovered: 152217
- Ever alive: 27964
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
