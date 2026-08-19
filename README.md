# SyndProxy private pool

## Current pool

- Alive now: 1218
- Gold now: 411
- HTTP: 453 alive / 91 gold
- HTTPS: 254 alive / 17 gold
- SOCKS4: 242 alive / 142 gold
- SOCKS5: 269 alive / 161 gold

## Historical pool

- Discovered: 131819
- Ever alive: 20933
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
