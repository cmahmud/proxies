# SyndProxy private pool

## Current pool

- Alive now: 843
- Gold now: 240
- HTTP: 249 alive / 29 gold
- HTTPS: 125 alive / 8 gold
- SOCKS4: 247 alive / 115 gold
- SOCKS5: 222 alive / 88 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6880
- Ever gold: 322

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
