# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 540
- HTTP: 365 alive / 161 gold
- HTTPS: 245 alive / 95 gold
- SOCKS4: 230 alive / 148 gold
- SOCKS5: 203 alive / 136 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18879
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
