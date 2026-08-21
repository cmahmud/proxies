# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 424
- HTTP: 329 alive / 106 gold
- HTTPS: 204 alive / 27 gold
- SOCKS4: 251 alive / 149 gold
- SOCKS5: 256 alive / 142 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30799
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
