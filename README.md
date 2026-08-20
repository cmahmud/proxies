# SyndProxy private pool

## Current pool

- Alive now: 1431
- Gold now: 582
- HTTP: 538 alive / 180 gold
- HTTPS: 385 alive / 93 gold
- SOCKS4: 244 alive / 142 gold
- SOCKS5: 264 alive / 167 gold

## Historical pool

- Discovered: 138941
- Ever alive: 23177
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
