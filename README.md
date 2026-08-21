# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 385
- HTTP: 314 alive / 77 gold
- HTTPS: 156 alive / 21 gold
- SOCKS4: 202 alive / 127 gold
- SOCKS5: 248 alive / 160 gold

## Historical pool

- Discovered: 157412
- Ever alive: 29698
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
