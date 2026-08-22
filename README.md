# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 419
- HTTP: 253 alive / 81 gold
- HTTPS: 204 alive / 25 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 276 alive / 172 gold

## Historical pool

- Discovered: 164957
- Ever alive: 32224
- Ever gold: 1176

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
