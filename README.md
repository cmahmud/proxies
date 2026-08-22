# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 426
- HTTP: 309 alive / 88 gold
- HTTPS: 236 alive / 27 gold
- SOCKS4: 203 alive / 145 gold
- SOCKS5: 254 alive / 166 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31231
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
