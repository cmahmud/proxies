# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 522
- HTTP: 402 alive / 146 gold
- HTTPS: 249 alive / 90 gold
- SOCKS4: 232 alive / 149 gold
- SOCKS5: 214 alive / 137 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17717
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
