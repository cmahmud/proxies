# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 416
- HTTP: 440 alive / 93 gold
- HTTPS: 221 alive / 31 gold
- SOCKS4: 220 alive / 133 gold
- SOCKS5: 248 alive / 159 gold

## Historical pool

- Discovered: 162773
- Ever alive: 31673
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
