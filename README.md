# SyndProxy private pool

## Current pool

- Alive now: 726
- Gold now: 374
- HTTP: 163 alive / 71 gold
- HTTPS: 139 alive / 18 gold
- SOCKS4: 226 alive / 149 gold
- SOCKS5: 198 alive / 136 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26254
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
