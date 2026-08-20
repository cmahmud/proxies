# SyndProxy private pool

## Current pool

- Alive now: 1740
- Gold now: 621
- HTTP: 658 alive / 216 gold
- HTTPS: 486 alive / 114 gold
- SOCKS4: 229 alive / 135 gold
- SOCKS5: 367 alive / 156 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23925
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
