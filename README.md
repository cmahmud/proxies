# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 312
- HTTP: 255 alive / 71 gold
- HTTPS: 137 alive / 21 gold
- SOCKS4: 174 alive / 104 gold
- SOCKS5: 185 alive / 116 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29767
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
