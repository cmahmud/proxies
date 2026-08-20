# SyndProxy private pool

## Current pool

- Alive now: 868
- Gold now: 400
- HTTP: 248 alive / 82 gold
- HTTPS: 207 alive / 23 gold
- SOCKS4: 204 alive / 144 gold
- SOCKS5: 209 alive / 151 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27160
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
