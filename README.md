# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 378
- HTTP: 427 alive / 84 gold
- HTTPS: 270 alive / 26 gold
- SOCKS4: 169 alive / 104 gold
- SOCKS5: 263 alive / 164 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32464
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
