# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 402
- HTTP: 267 alive / 100 gold
- HTTPS: 179 alive / 29 gold
- SOCKS4: 201 alive / 141 gold
- SOCKS5: 235 alive / 132 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31785
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
