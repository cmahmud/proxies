# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 406
- HTTP: 196 alive / 82 gold
- HTTPS: 138 alive / 26 gold
- SOCKS4: 199 alive / 135 gold
- SOCKS5: 237 alive / 163 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31395
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
