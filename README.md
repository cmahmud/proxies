# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 393
- HTTP: 331 alive / 86 gold
- HTTPS: 185 alive / 24 gold
- SOCKS4: 226 alive / 141 gold
- SOCKS5: 241 alive / 142 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29715
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
