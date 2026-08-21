# SyndProxy private pool

## Current pool

- Alive now: 1125
- Gold now: 402
- HTTP: 394 alive / 97 gold
- HTTPS: 292 alive / 30 gold
- SOCKS4: 220 alive / 153 gold
- SOCKS5: 219 alive / 122 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30324
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
