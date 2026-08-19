# SyndProxy private pool

## Current pool

- Alive now: 1152
- Gold now: 531
- HTTP: 419 alive / 157 gold
- HTTPS: 280 alive / 95 gold
- SOCKS4: 241 alive / 150 gold
- SOCKS5: 212 alive / 129 gold

## Historical pool

- Discovered: 123176
- Ever alive: 18909
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
