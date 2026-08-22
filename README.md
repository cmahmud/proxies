# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 394
- HTTP: 321 alive / 89 gold
- HTTPS: 230 alive / 24 gold
- SOCKS4: 204 alive / 112 gold
- SOCKS5: 257 alive / 169 gold

## Historical pool

- Discovered: 166616
- Ever alive: 32441
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
