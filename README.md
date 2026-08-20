# SyndProxy private pool

## Current pool

- Alive now: 709
- Gold now: 380
- HTTP: 174 alive / 64 gold
- HTTPS: 111 alive / 19 gold
- SOCKS4: 197 alive / 149 gold
- SOCKS5: 227 alive / 148 gold

## Historical pool

- Discovered: 147597
- Ever alive: 25862
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
