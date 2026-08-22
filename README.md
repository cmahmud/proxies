# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 426
- HTTP: 283 alive / 88 gold
- HTTPS: 221 alive / 27 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 282 alive / 168 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32209
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
