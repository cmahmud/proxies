# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 371
- HTTP: 181 alive / 66 gold
- HTTPS: 183 alive / 17 gold
- SOCKS4: 208 alive / 151 gold
- SOCKS5: 194 alive / 137 gold

## Historical pool

- Discovered: 147686
- Ever alive: 25923
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
