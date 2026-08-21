# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 365
- HTTP: 261 alive / 82 gold
- HTTPS: 226 alive / 25 gold
- SOCKS4: 205 alive / 123 gold
- SOCKS5: 202 alive / 135 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29803
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
