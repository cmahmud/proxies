# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 373
- HTTP: 281 alive / 84 gold
- HTTPS: 231 alive / 28 gold
- SOCKS4: 188 alive / 124 gold
- SOCKS5: 229 alive / 137 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28855
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
