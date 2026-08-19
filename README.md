# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 529
- HTTP: 411 alive / 161 gold
- HTTPS: 256 alive / 88 gold
- SOCKS4: 224 alive / 152 gold
- SOCKS5: 200 alive / 128 gold

## Historical pool

- Discovered: 119819
- Ever alive: 18202
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
