# SyndProxy private pool

## Current pool

- Alive now: 1307
- Gold now: 412
- HTTP: 470 alive / 92 gold
- HTTPS: 279 alive / 17 gold
- SOCKS4: 250 alive / 142 gold
- SOCKS5: 308 alive / 161 gold

## Historical pool

- Discovered: 131819
- Ever alive: 20938
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
