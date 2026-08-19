# SyndProxy private pool

## Current pool

- Alive now: 1134
- Gold now: 529
- HTTP: 437 alive / 160 gold
- HTTPS: 271 alive / 89 gold
- SOCKS4: 221 alive / 152 gold
- SOCKS5: 205 alive / 128 gold

## Historical pool

- Discovered: 119819
- Ever alive: 18208
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
