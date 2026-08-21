# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 409
- HTTP: 263 alive / 83 gold
- HTTPS: 190 alive / 24 gold
- SOCKS4: 206 alive / 150 gold
- SOCKS5: 240 alive / 152 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28919
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
