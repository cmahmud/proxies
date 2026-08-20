# SyndProxy private pool

## Current pool

- Alive now: 1372
- Gold now: 584
- HTTP: 487 alive / 188 gold
- HTTPS: 324 alive / 100 gold
- SOCKS4: 231 alive / 134 gold
- SOCKS5: 330 alive / 162 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23224
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
