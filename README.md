# SyndProxy private pool

## Current pool

- Alive now: 1143
- Gold now: 574
- HTTP: 367 alive / 187 gold
- HTTPS: 261 alive / 99 gold
- SOCKS4: 214 alive / 132 gold
- SOCKS5: 301 alive / 156 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23231
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
