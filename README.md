# SyndProxy private pool

## Current pool

- Alive now: 1124
- Gold now: 538
- HTTP: 437 alive / 166 gold
- HTTPS: 257 alive / 93 gold
- SOCKS4: 223 alive / 144 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18861
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
