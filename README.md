# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 426
- HTTP: 318 alive / 87 gold
- HTTPS: 266 alive / 28 gold
- SOCKS4: 240 alive / 147 gold
- SOCKS5: 259 alive / 164 gold

## Historical pool

- Discovered: 158927
- Ever alive: 30149
- Ever gold: 1142

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
