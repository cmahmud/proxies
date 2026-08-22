# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 406
- HTTP: 286 alive / 91 gold
- HTTPS: 171 alive / 26 gold
- SOCKS4: 219 alive / 146 gold
- SOCKS5: 227 alive / 143 gold

## Historical pool

- Discovered: 163255
- Ever alive: 31765
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
