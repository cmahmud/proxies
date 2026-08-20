# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 418
- HTTP: 240 alive / 78 gold
- HTTPS: 153 alive / 26 gold
- SOCKS4: 225 alive / 153 gold
- SOCKS5: 223 alive / 161 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27387
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
