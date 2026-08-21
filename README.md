# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 374
- HTTP: 256 alive / 90 gold
- HTTPS: 178 alive / 24 gold
- SOCKS4: 199 alive / 148 gold
- SOCKS5: 203 alive / 112 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28932
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
