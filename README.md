# SyndProxy private pool

## Current pool

- Alive now: 622
- Gold now: 383
- HTTP: 146 alive / 62 gold
- HTTPS: 71 alive / 13 gold
- SOCKS4: 199 alive / 152 gold
- SOCKS5: 206 alive / 156 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25719
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
