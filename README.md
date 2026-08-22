# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 413
- HTTP: 261 alive / 96 gold
- HTTPS: 174 alive / 29 gold
- SOCKS4: 214 alive / 144 gold
- SOCKS5: 219 alive / 144 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31764
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
