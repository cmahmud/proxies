# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 351
- HTTP: 113 alive / 44 gold
- HTTPS: 69 alive / 12 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 179 alive / 142 gold

## Historical pool

- Discovered: 171037
- Ever alive: 32809
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
