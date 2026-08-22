# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 394
- HTTP: 327 alive / 88 gold
- HTTPS: 232 alive / 24 gold
- SOCKS4: 196 alive / 111 gold
- SOCKS5: 259 alive / 171 gold

## Historical pool

- Discovered: 166616
- Ever alive: 32443
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
