# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 388
- HTTP: 237 alive / 78 gold
- HTTPS: 191 alive / 19 gold
- SOCKS4: 211 alive / 148 gold
- SOCKS5: 205 alive / 143 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26820
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
