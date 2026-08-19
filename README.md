# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 474
- HTTP: 323 alive / 118 gold
- HTTPS: 229 alive / 89 gold
- SOCKS4: 191 alive / 130 gold
- SOCKS5: 232 alive / 137 gold

## Historical pool

- Discovered: 117131
- Ever alive: 17545
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
