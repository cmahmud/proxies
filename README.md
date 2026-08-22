# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 387
- HTTP: 337 alive / 76 gold
- HTTPS: 222 alive / 26 gold
- SOCKS4: 236 alive / 121 gold
- SOCKS5: 256 alive / 164 gold

## Historical pool

- Discovered: 164965
- Ever alive: 32245
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
