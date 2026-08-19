# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 489
- HTTP: 358 alive / 134 gold
- HTTPS: 254 alive / 79 gold
- SOCKS4: 199 alive / 122 gold
- SOCKS5: 231 alive / 154 gold

## Historical pool

- Discovered: 119695
- Ever alive: 17866
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
