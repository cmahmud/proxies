# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 369
- HTTP: 182 alive / 64 gold
- HTTPS: 158 alive / 18 gold
- SOCKS4: 206 alive / 151 gold
- SOCKS5: 194 alive / 136 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25927
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
