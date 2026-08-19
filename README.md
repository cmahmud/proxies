# SyndProxy private pool

## Current pool

- Alive now: 1116
- Gold now: 462
- HTTP: 424 alive / 120 gold
- HTTPS: 262 alive / 75 gold
- SOCKS4: 204 alive / 140 gold
- SOCKS5: 226 alive / 127 gold

## Historical pool

- Discovered: 113546
- Ever alive: 16662
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
