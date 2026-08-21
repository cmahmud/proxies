# SyndProxy private pool

## Current pool

- Alive now: 932
- Gold now: 399
- HTTP: 306 alive / 84 gold
- HTTPS: 172 alive / 27 gold
- SOCKS4: 229 alive / 142 gold
- SOCKS5: 225 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29727
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
