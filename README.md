# SyndProxy private pool

## Current pool

- Alive now: 1157
- Gold now: 470
- HTTP: 434 alive / 125 gold
- HTTPS: 266 alive / 70 gold
- SOCKS4: 202 alive / 131 gold
- SOCKS5: 255 alive / 144 gold

## Historical pool

- Discovered: 117107
- Ever alive: 17201
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
