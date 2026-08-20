# SyndProxy private pool

## Current pool

- Alive now: 1285
- Gold now: 559
- HTTP: 476 alive / 188 gold
- HTTPS: 347 alive / 93 gold
- SOCKS4: 243 alive / 146 gold
- SOCKS5: 219 alive / 132 gold

## Historical pool

- Discovered: 137899
- Ever alive: 22922
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
