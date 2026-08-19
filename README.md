# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 503
- HTTP: 339 alive / 144 gold
- HTTPS: 260 alive / 80 gold
- SOCKS4: 238 alive / 147 gold
- SOCKS5: 207 alive / 132 gold

## Historical pool

- Discovered: 119697
- Ever alive: 17928
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
