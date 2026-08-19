# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 369
- HTTP: 321 alive / 62 gold
- HTTPS: 245 alive / 19 gold
- SOCKS4: 211 alive / 127 gold
- SOCKS5: 231 alive / 161 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15686
- Ever gold: 501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
