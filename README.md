# SyndProxy private pool

## Current pool

- Alive now: 1119
- Gold now: 424
- HTTP: 395 alive / 98 gold
- HTTPS: 287 alive / 32 gold
- SOCKS4: 194 alive / 132 gold
- SOCKS5: 243 alive / 162 gold

## Historical pool

- Discovered: 161019
- Ever alive: 31117
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
