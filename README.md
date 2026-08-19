# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 530
- HTTP: 383 alive / 160 gold
- HTTPS: 240 alive / 92 gold
- SOCKS4: 218 alive / 151 gold
- SOCKS5: 207 alive / 127 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18985
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
