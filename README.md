# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 547
- HTTP: 364 alive / 166 gold
- HTTPS: 235 alive / 90 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 206 alive / 147 gold

## Historical pool

- Discovered: 124825
- Ever alive: 19155
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
