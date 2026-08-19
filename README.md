# SyndProxy private pool

## Current pool

- Alive now: 1106
- Gold now: 550
- HTTP: 417 alive / 188 gold
- HTTPS: 281 alive / 103 gold
- SOCKS4: 203 alive / 121 gold
- SOCKS5: 205 alive / 138 gold

## Historical pool

- Discovered: 124841
- Ever alive: 19301
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
