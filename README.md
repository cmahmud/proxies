# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 412
- HTTP: 331 alive / 98 gold
- HTTPS: 260 alive / 24 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 236 alive / 144 gold

## Historical pool

- Discovered: 152750
- Ever alive: 28239
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
