# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 468
- HTTP: 380 alive / 127 gold
- HTTPS: 245 alive / 67 gold
- SOCKS4: 197 alive / 131 gold
- SOCKS5: 250 alive / 143 gold

## Historical pool

- Discovered: 117107
- Ever alive: 17151
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
