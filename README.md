# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 409
- HTTP: 362 alive / 89 gold
- HTTPS: 231 alive / 33 gold
- SOCKS4: 204 alive / 129 gold
- SOCKS5: 239 alive / 158 gold

## Historical pool

- Discovered: 163240
- Ever alive: 31690
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
