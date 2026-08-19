# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 368
- HTTP: 330 alive / 64 gold
- HTTPS: 224 alive / 18 gold
- SOCKS4: 226 alive / 128 gold
- SOCKS5: 235 alive / 158 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15669
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
