# SyndProxy private pool

## Current pool

- Alive now: 1168
- Gold now: 415
- HTTP: 398 alive / 105 gold
- HTTPS: 308 alive / 30 gold
- SOCKS4: 230 alive / 153 gold
- SOCKS5: 232 alive / 127 gold

## Historical pool

- Discovered: 159262
- Ever alive: 30330
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
