# SyndProxy private pool

## Current pool

- Alive now: 1112
- Gold now: 535
- HTTP: 386 alive / 162 gold
- HTTPS: 272 alive / 91 gold
- SOCKS4: 235 alive / 145 gold
- SOCKS5: 219 alive / 137 gold

## Historical pool

- Discovered: 123171
- Ever alive: 18895
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
