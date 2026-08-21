# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 403
- HTTP: 260 alive / 77 gold
- HTTPS: 196 alive / 21 gold
- SOCKS4: 216 alive / 145 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 155790
- Ever alive: 29328
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
