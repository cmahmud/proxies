# SyndProxy private pool

## Current pool

- Alive now: 1105
- Gold now: 392
- HTTP: 354 alive / 104 gold
- HTTPS: 253 alive / 23 gold
- SOCKS4: 201 alive / 121 gold
- SOCKS5: 297 alive / 144 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22630
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
