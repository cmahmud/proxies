# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 375
- HTTP: 396 alive / 93 gold
- HTTPS: 267 alive / 14 gold
- SOCKS4: 229 alive / 136 gold
- SOCKS5: 299 alive / 132 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20989
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
