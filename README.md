# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 364
- HTTP: 278 alive / 80 gold
- HTTPS: 227 alive / 20 gold
- SOCKS4: 181 alive / 115 gold
- SOCKS5: 243 alive / 149 gold

## Historical pool

- Discovered: 158224
- Ever alive: 29859
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
