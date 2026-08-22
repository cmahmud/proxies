# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 416
- HTTP: 374 alive / 90 gold
- HTTPS: 225 alive / 29 gold
- SOCKS4: 229 alive / 144 gold
- SOCKS5: 249 alive / 153 gold

## Historical pool

- Discovered: 164926
- Ever alive: 32164
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
