# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 400
- HTTP: 191 alive / 88 gold
- HTTPS: 114 alive / 21 gold
- SOCKS4: 203 alive / 146 gold
- SOCKS5: 232 alive / 145 gold

## Historical pool

- Discovered: 154725
- Ever alive: 29141
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
