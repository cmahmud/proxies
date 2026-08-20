# SyndProxy private pool

## Current pool

- Alive now: 802
- Gold now: 393
- HTTP: 233 alive / 83 gold
- HTTPS: 156 alive / 22 gold
- SOCKS4: 203 alive / 136 gold
- SOCKS5: 210 alive / 152 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27169
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
