# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 383
- HTTP: 198 alive / 76 gold
- HTTPS: 163 alive / 21 gold
- SOCKS4: 229 alive / 148 gold
- SOCKS5: 223 alive / 138 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26894
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
