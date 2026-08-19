# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 526
- HTTP: 371 alive / 154 gold
- HTTPS: 278 alive / 89 gold
- SOCKS4: 214 alive / 149 gold
- SOCKS5: 199 alive / 134 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17736
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
