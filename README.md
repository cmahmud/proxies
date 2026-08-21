# SyndProxy private pool

## Current pool

- Alive now: 1136
- Gold now: 399
- HTTP: 394 alive / 98 gold
- HTTPS: 302 alive / 29 gold
- SOCKS4: 226 alive / 151 gold
- SOCKS5: 214 alive / 121 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30314
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
