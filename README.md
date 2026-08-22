# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 421
- HTTP: 352 alive / 99 gold
- HTTPS: 253 alive / 32 gold
- SOCKS4: 186 alive / 134 gold
- SOCKS5: 247 alive / 156 gold

## Historical pool

- Discovered: 161018
- Ever alive: 31107
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
