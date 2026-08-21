# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 403
- HTTP: 279 alive / 97 gold
- HTTPS: 230 alive / 33 gold
- SOCKS4: 225 alive / 143 gold
- SOCKS5: 254 alive / 130 gold

## Historical pool

- Discovered: 160995
- Ever alive: 30939
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
