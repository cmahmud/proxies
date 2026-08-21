# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 357
- HTTP: 288 alive / 76 gold
- HTTPS: 190 alive / 18 gold
- SOCKS4: 199 alive / 127 gold
- SOCKS5: 248 alive / 136 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29849
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
