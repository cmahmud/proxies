# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 488
- HTTP: 411 alive / 118 gold
- HTTPS: 299 alive / 70 gold
- SOCKS4: 219 alive / 152 gold
- SOCKS5: 262 alive / 148 gold

## Historical pool

- Discovered: 116452
- Ever alive: 17108
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
