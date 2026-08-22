# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 422
- HTTP: 316 alive / 84 gold
- HTTPS: 195 alive / 29 gold
- SOCKS4: 216 alive / 138 gold
- SOCKS5: 265 alive / 171 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32236
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
