# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 411
- HTTP: 371 alive / 91 gold
- HTTPS: 237 alive / 37 gold
- SOCKS4: 221 alive / 142 gold
- SOCKS5: 236 alive / 141 gold

## Historical pool

- Discovered: 163249
- Ever alive: 31715
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
