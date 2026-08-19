# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 391
- HTTP: 362 alive / 104 gold
- HTTPS: 247 alive / 22 gold
- SOCKS4: 211 alive / 121 gold
- SOCKS5: 298 alive / 144 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22631
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
