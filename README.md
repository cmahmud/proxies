# SyndProxy private pool

## Current pool

- Alive now: 932
- Gold now: 333
- HTTP: 267 alive / 59 gold
- HTTPS: 216 alive / 12 gold
- SOCKS4: 233 alive / 139 gold
- SOCKS5: 216 alive / 123 gold

## Historical pool

- Discovered: 129286
- Ever alive: 20266
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
