# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 314
- HTTP: 241 alive / 75 gold
- HTTPS: 131 alive / 22 gold
- SOCKS4: 175 alive / 102 gold
- SOCKS5: 190 alive / 115 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29767
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
