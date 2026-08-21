# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 443
- HTTP: 354 alive / 108 gold
- HTTPS: 265 alive / 28 gold
- SOCKS4: 208 alive / 153 gold
- SOCKS5: 257 alive / 154 gold

## Historical pool

- Discovered: 153725
- Ever alive: 28565
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
