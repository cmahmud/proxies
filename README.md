# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 356
- HTTP: 313 alive / 76 gold
- HTTPS: 200 alive / 19 gold
- SOCKS4: 199 alive / 126 gold
- SOCKS5: 238 alive / 135 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29853
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
