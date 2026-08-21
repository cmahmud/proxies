# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 435
- HTTP: 336 alive / 106 gold
- HTTPS: 247 alive / 28 gold
- SOCKS4: 210 alive / 134 gold
- SOCKS5: 263 alive / 167 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30653
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
