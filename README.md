# SyndProxy private pool

## Current pool

- Alive now: 835
- Gold now: 369
- HTTP: 209 alive / 74 gold
- HTTPS: 194 alive / 17 gold
- SOCKS4: 197 alive / 118 gold
- SOCKS5: 235 alive / 160 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26117
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
