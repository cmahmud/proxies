# SyndProxy private pool

## Current pool

- Alive now: 1120
- Gold now: 540
- HTTP: 391 alive / 163 gold
- HTTPS: 272 alive / 95 gold
- SOCKS4: 235 alive / 145 gold
- SOCKS5: 222 alive / 137 gold

## Historical pool

- Discovered: 123171
- Ever alive: 18891
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
