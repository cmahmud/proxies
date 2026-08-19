# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 487
- HTTP: 368 alive / 132 gold
- HTTPS: 258 alive / 79 gold
- SOCKS4: 209 alive / 122 gold
- SOCKS5: 234 alive / 154 gold

## Historical pool

- Discovered: 119695
- Ever alive: 17866
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
