# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 420
- HTTP: 208 alive / 88 gold
- HTTPS: 135 alive / 24 gold
- SOCKS4: 223 alive / 153 gold
- SOCKS5: 241 alive / 155 gold

## Historical pool

- Discovered: 155686
- Ever alive: 29217
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
