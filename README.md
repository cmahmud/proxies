# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 399
- HTTP: 329 alive / 88 gold
- HTTPS: 183 alive / 28 gold
- SOCKS4: 208 alive / 146 gold
- SOCKS5: 242 alive / 137 gold

## Historical pool

- Discovered: 167118
- Ever alive: 32529
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
