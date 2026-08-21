# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 393
- HTTP: 224 alive / 90 gold
- HTTPS: 224 alive / 20 gold
- SOCKS4: 187 alive / 137 gold
- SOCKS5: 213 alive / 146 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27876
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
