# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 395
- HTTP: 329 alive / 89 gold
- HTTPS: 261 alive / 24 gold
- SOCKS4: 192 alive / 111 gold
- SOCKS5: 256 alive / 171 gold

## Historical pool

- Discovered: 166616
- Ever alive: 32443
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
