# SyndProxy private pool

## Current pool

- Alive now: 1087
- Gold now: 425
- HTTP: 334 alive / 87 gold
- HTTPS: 256 alive / 27 gold
- SOCKS4: 227 alive / 147 gold
- SOCKS5: 270 alive / 164 gold

## Historical pool

- Discovered: 158927
- Ever alive: 30145
- Ever gold: 1142

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
