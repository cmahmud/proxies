# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 394
- HTTP: 299 alive / 72 gold
- HTTPS: 227 alive / 15 gold
- SOCKS4: 250 alive / 152 gold
- SOCKS5: 242 alive / 155 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20419
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
