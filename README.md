# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 552
- HTTP: 365 alive / 163 gold
- HTTPS: 272 alive / 90 gold
- SOCKS4: 225 alive / 151 gold
- SOCKS5: 223 alive / 148 gold

## Historical pool

- Discovered: 123175
- Ever alive: 18895
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
