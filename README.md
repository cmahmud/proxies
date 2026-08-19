# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 524
- HTTP: 406 alive / 147 gold
- HTTPS: 243 alive / 90 gold
- SOCKS4: 235 alive / 151 gold
- SOCKS5: 213 alive / 136 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17717
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
