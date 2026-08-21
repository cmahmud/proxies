# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 411
- HTTP: 318 alive / 96 gold
- HTTPS: 203 alive / 27 gold
- SOCKS4: 221 alive / 142 gold
- SOCKS5: 247 alive / 146 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29721
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
