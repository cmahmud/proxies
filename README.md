# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 420
- HTTP: 335 alive / 94 gold
- HTTPS: 234 alive / 25 gold
- SOCKS4: 235 alive / 150 gold
- SOCKS5: 245 alive / 151 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25166
- Ever gold: 1056

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
