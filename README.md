# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 474
- HTTP: 376 alive / 136 gold
- HTTPS: 231 alive / 90 gold
- SOCKS4: 224 alive / 137 gold
- SOCKS5: 211 alive / 111 gold

## Historical pool

- Discovered: 117124
- Ever alive: 17430
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
