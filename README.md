# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 404
- HTTP: 290 alive / 97 gold
- HTTPS: 221 alive / 34 gold
- SOCKS4: 214 alive / 143 gold
- SOCKS5: 239 alive / 130 gold

## Historical pool

- Discovered: 160995
- Ever alive: 30944
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
