# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 420
- HTTP: 297 alive / 91 gold
- HTTPS: 173 alive / 25 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 271 alive / 163 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29037
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
