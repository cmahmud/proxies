# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 425
- HTTP: 299 alive / 108 gold
- HTTPS: 209 alive / 27 gold
- SOCKS4: 238 alive / 149 gold
- SOCKS5: 254 alive / 141 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30801
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
