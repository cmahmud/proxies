# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 285
- HTTP: 247 alive / 25 gold
- HTTPS: 150 alive / 4 gold
- SOCKS4: 241 alive / 143 gold
- SOCKS5: 232 alive / 113 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12337
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
