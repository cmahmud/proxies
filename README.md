# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 463
- HTTP: 128 alive / 93 gold
- HTTPS: 138 alive / 32 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 213 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46006
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
