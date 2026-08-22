# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 422
- HTTP: 291 alive / 83 gold
- HTTPS: 211 alive / 26 gold
- SOCKS4: 223 alive / 152 gold
- SOCKS5: 254 alive / 161 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32000
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
