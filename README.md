# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 520
- HTTP: 347 alive / 159 gold
- HTTPS: 251 alive / 91 gold
- SOCKS4: 211 alive / 149 gold
- SOCKS5: 202 alive / 121 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18998
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
