# SyndProxy private pool

## Current pool

- Alive now: 926
- Gold now: 406
- HTTP: 270 alive / 95 gold
- HTTPS: 221 alive / 31 gold
- SOCKS4: 212 alive / 150 gold
- SOCKS5: 223 alive / 130 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30958
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
