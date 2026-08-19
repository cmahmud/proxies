# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 482
- HTTP: 334 alive / 126 gold
- HTTPS: 266 alive / 79 gold
- SOCKS4: 215 alive / 125 gold
- SOCKS5: 223 alive / 152 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17893
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
