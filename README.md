# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 417
- HTTP: 211 alive / 91 gold
- HTTPS: 155 alive / 31 gold
- SOCKS4: 203 alive / 132 gold
- SOCKS5: 256 alive / 163 gold

## Historical pool

- Discovered: 162771
- Ever alive: 31640
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
