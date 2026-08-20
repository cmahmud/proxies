# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 371
- HTTP: 242 alive / 69 gold
- HTTPS: 132 alive / 17 gold
- SOCKS4: 211 alive / 149 gold
- SOCKS5: 208 alive / 136 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25482
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
