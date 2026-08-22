# SyndProxy private pool

## Current pool

- Alive now: 722
- Gold now: 403
- HTTP: 188 alive / 95 gold
- HTTPS: 131 alive / 28 gold
- SOCKS4: 174 alive / 128 gold
- SOCKS5: 229 alive / 152 gold

## Historical pool

- Discovered: 163842
- Ever alive: 31919
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
