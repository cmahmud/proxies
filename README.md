# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 523
- HTTP: 399 alive / 163 gold
- HTTPS: 232 alive / 90 gold
- SOCKS4: 224 alive / 146 gold
- SOCKS5: 206 alive / 124 gold

## Historical pool

- Discovered: 123233
- Ever alive: 19009
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
