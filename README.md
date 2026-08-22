# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 366
- HTTP: 295 alive / 76 gold
- HTTPS: 247 alive / 26 gold
- SOCKS4: 180 alive / 123 gold
- SOCKS5: 225 alive / 141 gold

## Historical pool

- Discovered: 165755
- Ever alive: 32302
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
