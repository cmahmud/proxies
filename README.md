# SyndProxy private pool

## Current pool

- Alive now: 1057
- Gold now: 419
- HTTP: 354 alive / 95 gold
- HTTPS: 283 alive / 33 gold
- SOCKS4: 185 alive / 130 gold
- SOCKS5: 235 alive / 161 gold

## Historical pool

- Discovered: 161344
- Ever alive: 31120
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
