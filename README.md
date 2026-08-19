# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 369
- HTTP: 303 alive / 63 gold
- HTTPS: 246 alive / 18 gold
- SOCKS4: 206 alive / 127 gold
- SOCKS5: 238 alive / 161 gold

## Historical pool

- Discovered: 110416
- Ever alive: 15719
- Ever gold: 502

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
