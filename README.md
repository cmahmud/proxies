# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 254
- HTTP: 223 alive / 33 gold
- HTTPS: 98 alive / 3 gold
- SOCKS4: 209 alive / 116 gold
- SOCKS5: 212 alive / 102 gold

## Historical pool

- Discovered: 95402
- Ever alive: 10699
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
