# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 417
- HTTP: 89 alive / 62 gold
- HTTPS: 88 alive / 21 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36093
- Ever gold: 1267

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
