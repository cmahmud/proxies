# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 420
- HTTP: 322 alive / 96 gold
- HTTPS: 208 alive / 26 gold
- SOCKS4: 214 alive / 138 gold
- SOCKS5: 274 alive / 160 gold

## Historical pool

- Discovered: 154717
- Ever alive: 29024
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
