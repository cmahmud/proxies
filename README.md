# SyndProxy private pool

## Current pool

- Alive now: 779
- Gold now: 358
- HTTP: 229 alive / 86 gold
- HTTPS: 141 alive / 29 gold
- SOCKS4: 188 alive / 114 gold
- SOCKS5: 221 alive / 129 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32572
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
