# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 540
- HTTP: 404 alive / 164 gold
- HTTPS: 280 alive / 94 gold
- SOCKS4: 233 alive / 145 gold
- SOCKS5: 222 alive / 137 gold

## Historical pool

- Discovered: 123171
- Ever alive: 18895
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
