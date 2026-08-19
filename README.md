# SyndProxy private pool

## Current pool

- Alive now: 1153
- Gold now: 541
- HTTP: 449 alive / 168 gold
- HTTPS: 255 alive / 93 gold
- SOCKS4: 238 alive / 143 gold
- SOCKS5: 211 alive / 137 gold

## Historical pool

- Discovered: 123170
- Ever alive: 18864
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
