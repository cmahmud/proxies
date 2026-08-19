# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 540
- HTTP: 410 alive / 163 gold
- HTTPS: 277 alive / 89 gold
- SOCKS4: 225 alive / 145 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 123921
- Ever alive: 19146
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
