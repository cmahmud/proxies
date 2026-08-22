# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 410
- HTTP: 260 alive / 89 gold
- HTTPS: 156 alive / 27 gold
- SOCKS4: 230 alive / 148 gold
- SOCKS5: 225 alive / 146 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32386
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
