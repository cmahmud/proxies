# SyndProxy private pool

## Current pool

- Alive now: 809
- Gold now: 414
- HTTP: 227 alive / 94 gold
- HTTPS: 174 alive / 21 gold
- SOCKS4: 189 alive / 147 gold
- SOCKS5: 219 alive / 152 gold

## Historical pool

- Discovered: 152161
- Ever alive: 27850
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
