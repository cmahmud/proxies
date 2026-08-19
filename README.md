# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 479
- HTTP: 335 alive / 123 gold
- HTTPS: 222 alive / 70 gold
- SOCKS4: 221 alive / 138 gold
- SOCKS5: 258 alive / 148 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16871
- Ever gold: 625

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
