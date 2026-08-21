# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 409
- HTTP: 338 alive / 88 gold
- HTTPS: 197 alive / 23 gold
- SOCKS4: 212 alive / 153 gold
- SOCKS5: 247 alive / 145 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30073
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
