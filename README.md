# SyndProxy private pool

## Current pool

- Alive now: 657
- Gold now: 352
- HTTP: 162 alive / 69 gold
- HTTPS: 113 alive / 22 gold
- SOCKS4: 191 alive / 122 gold
- SOCKS5: 191 alive / 139 gold

## Historical pool

- Discovered: 145582
- Ever alive: 25585
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
