# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 400
- HTTP: 266 alive / 93 gold
- HTTPS: 202 alive / 31 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 230 alive / 130 gold

## Historical pool

- Discovered: 161006
- Ever alive: 30993
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
