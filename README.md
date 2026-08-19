# SyndProxy private pool

## Current pool

- Alive now: 1226
- Gold now: 403
- HTTP: 397 alive / 76 gold
- HTTPS: 269 alive / 12 gold
- SOCKS4: 294 alive / 151 gold
- SOCKS5: 266 alive / 164 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20669
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
