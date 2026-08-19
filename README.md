# SyndProxy private pool

## Current pool

- Alive now: 1180
- Gold now: 401
- HTTP: 370 alive / 75 gold
- HTTPS: 258 alive / 12 gold
- SOCKS4: 288 alive / 150 gold
- SOCKS5: 264 alive / 164 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20669
- Ever gold: 872

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
