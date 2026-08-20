# SyndProxy private pool

## Current pool

- Alive now: 1468
- Gold now: 610
- HTTP: 556 alive / 221 gold
- HTTPS: 463 alive / 117 gold
- SOCKS4: 212 alive / 133 gold
- SOCKS5: 237 alive / 139 gold

## Historical pool

- Discovered: 141134
- Ever alive: 23800
- Ever gold: 961

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
