# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 479
- HTTP: 329 alive / 125 gold
- HTTPS: 264 alive / 78 gold
- SOCKS4: 217 alive / 125 gold
- SOCKS5: 227 alive / 151 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17897
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
