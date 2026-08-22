# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 407
- HTTP: 283 alive / 93 gold
- HTTPS: 181 alive / 28 gold
- SOCKS4: 199 alive / 145 gold
- SOCKS5: 229 alive / 141 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32532
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
