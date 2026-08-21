# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 392
- HTTP: 332 alive / 84 gold
- HTTPS: 193 alive / 24 gold
- SOCKS4: 219 alive / 141 gold
- SOCKS5: 249 alive / 143 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29715
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
