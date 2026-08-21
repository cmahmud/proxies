# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 398
- HTTP: 334 alive / 88 gold
- HTTPS: 174 alive / 20 gold
- SOCKS4: 204 alive / 129 gold
- SOCKS5: 252 alive / 161 gold

## Historical pool

- Discovered: 157414
- Ever alive: 29710
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
