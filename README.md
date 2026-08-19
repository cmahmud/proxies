# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 546
- HTTP: 350 alive / 169 gold
- HTTPS: 230 alive / 90 gold
- SOCKS4: 211 alive / 151 gold
- SOCKS5: 198 alive / 136 gold

## Historical pool

- Discovered: 123235
- Ever alive: 19037
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
