# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 400
- HTTP: 335 alive / 86 gold
- HTTPS: 193 alive / 22 gold
- SOCKS4: 198 alive / 129 gold
- SOCKS5: 257 alive / 163 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29710
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
