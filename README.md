# SyndProxy private pool

## Current pool

- Alive now: 1229
- Gold now: 416
- HTTP: 449 alive / 105 gold
- HTTPS: 304 alive / 28 gold
- SOCKS4: 242 alive / 152 gold
- SOCKS5: 234 alive / 131 gold

## Historical pool

- Discovered: 159262
- Ever alive: 30335
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
