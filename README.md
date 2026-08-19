# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 522
- HTTP: 405 alive / 154 gold
- HTTPS: 269 alive / 94 gold
- SOCKS4: 253 alive / 148 gold
- SOCKS5: 212 alive / 126 gold

## Historical pool

- Discovered: 123176
- Ever alive: 18919
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
