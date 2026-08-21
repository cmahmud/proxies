# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 352
- HTTP: 349 alive / 73 gold
- HTTPS: 197 alive / 18 gold
- SOCKS4: 209 alive / 127 gold
- SOCKS5: 245 alive / 134 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29852
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
