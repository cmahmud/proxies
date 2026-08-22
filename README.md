# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 411
- HTTP: 374 alive / 90 gold
- HTTPS: 238 alive / 34 gold
- SOCKS4: 199 alive / 129 gold
- SOCKS5: 235 alive / 158 gold

## Historical pool

- Discovered: 163240
- Ever alive: 31693
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
