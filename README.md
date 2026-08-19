# SyndProxy private pool

## Current pool

- Alive now: 1226
- Gold now: 403
- HTTP: 435 alive / 92 gold
- HTTPS: 298 alive / 15 gold
- SOCKS4: 243 alive / 132 gold
- SOCKS5: 250 alive / 164 gold

## Historical pool

- Discovered: 131862
- Ever alive: 21364
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
