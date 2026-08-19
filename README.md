# SyndProxy private pool

## Current pool

- Alive now: 1174
- Gold now: 496
- HTTP: 419 alive / 174 gold
- HTTPS: 317 alive / 69 gold
- SOCKS4: 227 alive / 128 gold
- SOCKS5: 211 alive / 125 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19768
- Ever gold: 778

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
