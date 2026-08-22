# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 421
- HTTP: 295 alive / 78 gold
- HTTPS: 232 alive / 26 gold
- SOCKS4: 221 alive / 142 gold
- SOCKS5: 273 alive / 175 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32227
- Ever gold: 1176

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
