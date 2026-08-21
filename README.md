# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 410
- HTTP: 268 alive / 81 gold
- HTTPS: 176 alive / 24 gold
- SOCKS4: 200 alive / 151 gold
- SOCKS5: 236 alive / 154 gold

## Historical pool

- Discovered: 154486
- Ever alive: 28909
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
