# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 403
- HTTP: 185 alive / 81 gold
- HTTPS: 148 alive / 30 gold
- SOCKS4: 204 alive / 148 gold
- SOCKS5: 210 alive / 144 gold

## Historical pool

- Discovered: 163333
- Ever alive: 31897
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
