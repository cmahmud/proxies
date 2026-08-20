# SyndProxy private pool

## Current pool

- Alive now: 733
- Gold now: 369
- HTTP: 182 alive / 64 gold
- HTTPS: 152 alive / 17 gold
- SOCKS4: 210 alive / 151 gold
- SOCKS5: 189 alive / 137 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25923
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
