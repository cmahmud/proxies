# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 487
- HTTP: 371 alive / 122 gold
- HTTPS: 229 alive / 74 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 259 alive / 150 gold

## Historical pool

- Discovered: 114274
- Ever alive: 16919
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
