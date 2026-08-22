# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 447
- HTTP: 299 alive / 86 gold
- HTTPS: 202 alive / 33 gold
- SOCKS4: 240 alive / 155 gold
- SOCKS5: 248 alive / 173 gold

## Historical pool

- Discovered: 163874
- Ever alive: 32018
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
