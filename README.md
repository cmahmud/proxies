# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 538
- HTTP: 368 alive / 159 gold
- HTTPS: 242 alive / 95 gold
- SOCKS4: 242 alive / 147 gold
- SOCKS5: 204 alive / 137 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18891
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
