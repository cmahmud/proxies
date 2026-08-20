# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 372
- HTTP: 244 alive / 67 gold
- HTTPS: 147 alive / 17 gold
- SOCKS4: 213 alive / 151 gold
- SOCKS5: 195 alive / 137 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25912
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
