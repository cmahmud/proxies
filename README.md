# SyndProxy private pool

## Current pool

- Alive now: 1175
- Gold now: 405
- HTTP: 392 alive / 76 gold
- HTTPS: 266 alive / 14 gold
- SOCKS4: 257 alive / 152 gold
- SOCKS5: 260 alive / 163 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20627
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
