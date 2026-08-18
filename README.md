# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 320
- HTTP: 257 alive / 36 gold
- HTTPS: 172 alive / 9 gold
- SOCKS4: 222 alive / 142 gold
- SOCKS5: 219 alive / 133 gold

## Historical pool

- Discovered: 103711
- Ever alive: 14013
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
