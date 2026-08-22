# SyndProxy private pool

## Current pool

- Alive now: 816
- Gold now: 406
- HTTP: 210 alive / 84 gold
- HTTPS: 162 alive / 26 gold
- SOCKS4: 196 alive / 138 gold
- SOCKS5: 248 alive / 158 gold

## Historical pool

- Discovered: 162241
- Ever alive: 31414
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
